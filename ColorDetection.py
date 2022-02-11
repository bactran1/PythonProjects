import cv2
import time
import numpy as np
url = "rtsp://192.168.10.228:8554/live"

width = 1280
height = 720

cap = cv2.VideoCapture(url)

cap.set(3, width)
cap.set(4, height)

while True:
    startTime = time.time()
    camera, frame = cap.read()

    FPS = int(1/(time.time()-startTime))

    if frame is not None:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        blurredFrame = cv2.GaussianBlur(frame, (5, 5), 0)
        HSVframe = cv2.cvtColor(blurredFrame, cv2.COLOR_BGR2HSV)

        #RED
        lowRed_HSV = np.array([166,155,84])
        highRed_HSV = np.array([179, 255, 255])


        #mask = cv2.inRange(frame, lowRed, highRed)
        red_mask = cv2.inRange(HSVframe, lowRed_HSV, highRed_HSV)

        redFrame = cv2.bitwise_and(frame, frame, mask=red_mask)

        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        #cv2.drawContours(frame, contours, -1, (0,255,0),3)

        #frame = cv2.putText(frame, f'FPS: {FPS}', [width-80, 50], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        #cv2.imshow('testIpCam', frame)
        cv2.imshow('Mask Red', frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()