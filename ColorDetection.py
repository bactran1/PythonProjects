import cv2
import time
import numpy as np
url = "rtsp://192.168.10.228:8554/live"
ipCamURL = 'rtsp://admin:elmore@10.1.10.53:554/ch02/01'

width = 1280
height = 720

#cap = cv2.VideoCapture(ipCamURL)
cap = cv2.VideoCapture(url)
#cap = cv2.VideoCapture(0)

cap.set(3, width)
cap.set(4, height)

while True:
    startTime = time.time()
    camera, frame = cap.read()

    FPS = int(1/(time.time()-startTime))

    if frame is not None:

        #frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        blurredFrame = cv2.GaussianBlur(frame, (5, 5), 0)
        HSVframe = cv2.cvtColor(blurredFrame, cv2.COLOR_BGR2HSV)

        #RED
        lowRed_HSV1 = np.array([0,70,50])
        highRed_HSV1 = np.array([10, 255, 255])
        lowRed_HSV2 = np.array([170,70,50])
        highRed_HSV2 = np.array([180, 255, 255])


        #mask = cv2.inRange(frame, lowRed, highRed)
        red_mask1 = cv2.inRange(HSVframe, lowRed_HSV1, highRed_HSV1)
        red_mask2 = cv2.inRange(HSVframe, lowRed_HSV2, highRed_HSV2)

        redFrame = cv2.bitwise_and(frame, frame, mask=red_mask1)
        red_mask = red_mask1 | red_mask2

        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #cv2.drawContours(frame, contours, -1, (0,255,0),3)

        frame = cv2.putText(frame, f'FPS: {FPS}', [width-130, 30], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        #cv2.imshow('testIpCam', frame)
        cv2.imshow('Mask Red', frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()