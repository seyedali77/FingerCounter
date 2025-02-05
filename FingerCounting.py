import time
import cv2
import mediapipe as mp
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # Set webcam width
cap.set(4, hCam)  # Set webcam height

# Load overlay images for fingers display
folderPath = "fingers"
myList = os.listdir(folderPath)
overlayList = []
for impath in myList:
    image = cv2.imread(f'{folderPath}/{impath}')
    overlayList.append(image)

pTime = 0  # For FPS calculation
detector = htm.handDetector(detectioncon=0.75)  # Initialize hand detector
tipsIds = [4, 8, 12, 16, 20]  # Landmark IDs for fingertips

while True:
    success, img = cap.read()
    img = detector.findHand(img)  # Detect and draw hand landmarks
    lmList = detector.findPosition(img, draw=False)

    totalFingers = 0
    if len(lmList) != 0:
        fingers = []
        # Thumb: check if it's open by comparing x positions
        if lmList[tipsIds[0]][1] > lmList[tipsIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # Fingers: check if they are open by comparing y positions
        for id in range(1, 5):
            if lmList[tipsIds[id]][2] < lmList[tipsIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers = sum(fingers)
        # Ensure index is within overlayList range
        if totalFingers >= len(overlayList):
            totalFingers = len(overlayList) - 1

    # Overlay the corresponding image on the webcam feed
    h, w, c = overlayList[totalFingers].shape
    img[0:h, 0:w] = overlayList[totalFingers]

    # Draw a rectangle and display finger count
    cv2.rectangle(img, (20,225), (178,425), (0,255,0), cv2.FILLED)
    cv2.putText(img, str(totalFingers), (45,375), cv2.FONT_HERSHEY_PLAIN, 10, (255,0,0), 25)

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (400,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
