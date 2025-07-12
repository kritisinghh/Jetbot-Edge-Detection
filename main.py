# pip install opencv-python numpy jetcam jetbot

import cv2
import time
import numpy as np
from jetcam.csi_camera import CSICamera
from jetbot import Robot

WIDTH, HEIGHT = 224, 224
CANNY_LOW, CANNY_HIGH = 50, 150
ROI_Y = 150
EDGE_PCT_THRESH = 0.05
FWD_SPEED = 0.25
TURN_SPEED = 0.25
BACK_OFF_TIME = 0.3
TURN_TIME = 0.45

def edge_fraction(edges):
    roi = edges[ROI_Y:, :]
    return np.count_nonzero(roi) / roi.size

def main():
    robot = Robot()
    camera = CSICamera(width=WIDTH, height=HEIGHT, capture_device=0)
    camera.running = True
    time.sleep(0.2)
    try:
        while True:
            frame = camera.value
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            edges = cv2.Canny(blur, CANNY_LOW, CANNY_HIGH)

            if edge_fraction(edges) > EDGE_PCT_THRESH:
                timestamp = int(time.time() * 1000)
                cv2.imwrite(f"edge_detected_{timestamp}.jpg", frame)
                robot.backward(FWD_SPEED)
                time.sleep(BACK_OFF_TIME)
                robot.right(TURN_SPEED)
                time.sleep(TURN_TIME)
                robot.stop()
            else:
                robot.forward(FWD_SPEED)
    except KeyboardInterrupt:
        pass
    finally:
        robot.stop()
        camera.running = False
        camera.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
