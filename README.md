# FingerCounter
Real-Time Finger Counting and Overlay Images
# Hand Tracking Finger Counter

This project uses OpenCV, MediaPipe, and a custom hand tracking module to detect a hand in real time using your webcam and count the number of fingers being held up. Based on the detected number, it overlays an image from a folder onto the video feed.

## Features

- **Real-Time Hand Detection:** Uses a hand tracking module (based on MediaPipe) to detect and draw hand landmarks.
- **Finger Counting:** Determines the number of fingers shown based on landmark positions.
- **Overlay Images:** Displays a corresponding image (from the `fingers` folder) based on the number of detected fingers.
- **FPS Display:** Calculates and shows the current frames per second (FPS) on the video feed.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe
- A custom hand tracking module (`HandTrackingModule.py`) 
- A folder named `fingers` containing the overlay images (e.g., images for 0-5 fingers)


