import random

import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
width = 1280
height = 720
detector = HandDetector(detectionCon=0.7)
picture = np.ones((height,width,3), dtype=np.uint8)
oldpoint = (0,0,0)
aktpoint = (0,0,0)
firsttime = True
while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)
    color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

    if lmList:
        cursor = lmList[8]  # cursor is indexfinger
        in_height = img.shape[0]
        in_width = img.shape[1]
        cursor_in_picture = (cursor[0]*height//in_height, cursor[1]*width//in_width)
        if firsttime:
            oldpoint=cursor_in_picture
            aktpoint=cursor_in_picture
            firsttime=False
        else:
            oldpoint=aktpoint
            aktpoint=cursor_in_picture
            cv2.line(picture,oldpoint, aktpoint, color, 5)

    cv2.imshow("picture", picture)
    cv2.waitKey(1)