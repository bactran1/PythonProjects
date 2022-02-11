import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import time

if torch.cuda.is_available():
    print('Cuda is available!')
else:
    print('Cuda is not available!')

width = 640
height = 480

# ipCamURL = 'rtsp://192.168.10.228:8554/live'
ipCamURL = 'rtsp://admin:elmore@10.1.10.53:554/ch04/01'


# Test if the camera is available
def testCam(source):
    cap = cv2.VideoCapture(source)
    if cap is None or not cap.isOpened():
        print('Warning: unable to open video source: ', source)
        return False
        # quit()
    else:
        # print(f'Camera available: {source}')
        return True


source = ''
if not testCam(0):
    if testCam(ipCamURL):
        print('Camera available!')
        source = ipCamURL
    else:
        print('No camera available!')
        quit()
else:
    print('Camera available!')
    source = 0

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(source)
cap.set(3, width)
cap.set(4, height)

reader = easyocr.Reader(['en'])

# Problem: when rotation_info is not None, result at 0 degree will be disregard. Try adding 3 more Readers
while True:
    startTime = time.time()

    success, imgOriginal = cap.read()
    img = np.asarray(imgOriginal)
    img = cv2.resize(img, (width, height))

    result = reader.readtext(img,
                             text_threshold=0.7,
                             rotation_info=None,
                             low_text=0.3,
                             link_threshold=0.5,
                             detail=1,
                             batch_size=32)

    print(result, len(result))

    numObjectDetected = len(result)

    font = cv2.FONT_HERSHEY_SIMPLEX

    spacer = 100
    FPS = int(1 / (time.time() - startTime))
    if numObjectDetected == 0:
        img = cv2.putText(img, f'FPS: {FPS}', (width - 125, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        img = cv2.putText(img, "No object detected!", (25, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    elif numObjectDetected >= 0:
        text = " "

        for i1 in range(numObjectDetected):
            if result[i1][2] < 0.8:
                result[i1] = [((0, 0), (0, 0), (0, 0), (0, 0)), '', 0.0]
                print("Below threshold!")
            else:
                for detection in result:
                    top_left = tuple([int(detection[0][0][0]), int(detection[0][0][1])])
                    bottom_right = tuple([int(detection[0][2][0]), int(detection[0][2][1])])
                    text = detection[1] + ' ' + str(100 * round(detection[2], 3))
                    img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
                    img = cv2.putText(img, text, top_left, font, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    img = cv2.putText(img, f'FPS: {FPS}', (width-125, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    spacer += 10

    cv2.imshow("Test Stream", img)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    # print(f'FPS: {FPS}')
