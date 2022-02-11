import cv2
import time
import numpy as np
url = "rtsp://192.168.10.228:8554/live"
cap = cv2.VideoCapture(url)
while True:
    startTime = time.time()
    camera, frame = cap.read()

    FPS = int(1/(time.time()-startTime))

    if frame is not None:
        frame = cv2.putText(frame, f'FPS: {FPS}', [1200,50], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('testIpCam', frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()