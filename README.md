# JetBot Edge Detection and Obstacle Avoidance 

This project uses the NVIDIA JetBot to **detect edges** in real-time using OpenCV and **avoid obstacles**. If a large number of edges (like a wall) is detected, the JetBot stops, backs up, and turns to avoid collision.

# How It Works

1. Camera Feed is captured using the CSI camera.
2. The image is grayscale converted and blurred to reduce noise.
3. Canny Edge Detection is applied.
4. If too many edges are detected in the bottom part of the image:
   - JetBot saves the image
   - Moves backward briefly
   - Turns right
5. Otherwise, it keeps moving forward.

# Hardware Needed:
- Jetson Nano
- JetBot Kit
- CSI Camera connected to Jetson

