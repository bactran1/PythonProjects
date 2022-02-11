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

width = 1280
height = 720

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

reader = easyocr.Reader(['en'])

#Problem: when rotation_info is not None, result at 0 degree will be disregard. Try adding 3 more Readers
while True:
    start_time = time.time()    #Start time to calculate fps

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

    if numObjectDetected == 0:
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
                    spacer += 10

    cv2.imshow("Test Stream", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    print(1.0/(time.time()-start_time))