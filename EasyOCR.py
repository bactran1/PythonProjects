#import os
#os.environ['KMP_DUPLICATE_LIB_OK']='True'
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

#IMAGE_PATH = open('sign.png', 'rb')
#source = IMAGE_PATH.read()

IMAGE_PATH = 'surf.jpeg'

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH, detail=1)
result


# top_left = tuple(result[0][0][0])
# bottom_right = tuple(result[0][0][2])
# text = result[0][1]
# font = cv2.FONT_HERSHEY_SIMPLEX

# img = cv2.imread(IMAGE_PATH)
# img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
# img = cv2.putText(img, text, top_left, font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
# plt.imshow(img)
# plt.show()
#
# img = cv2.imread(IMAGE_PATH)
# spacer = 100
# for detection in result:
#     top_left = tuple(detection[0][0])
#     bottom_right = tuple(detection[0][2])
#     text = detection[1]
#     img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
#     img = cv2.putText(img, text, (20, spacer), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
#     spacer += 15
#
# plt.imshow(img)
# plt.show()

