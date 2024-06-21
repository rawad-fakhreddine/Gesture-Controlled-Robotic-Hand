import cv2 as cv
import HandTrackingModule as htm
import SerialModule as sm
import time

cap = cv.VideoCapture(0)
detector = htm.handDetector(maxHands=1, detectionCon=0.7)
mySerial = sm.SerialObject("COM4", 9600, 1)

last_send_time = time.time()
delay = 0.1
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUP()
        # print(fingers)
        current_time = time.time()
        if current_time - last_send_time >= delay:
            mySerial.sendData(fingers)
            last_send_time = current_time 
        # print(s)
    cv.imshow("Image", img)
    cv.waitKey(1)