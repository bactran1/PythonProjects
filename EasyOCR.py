#import os
#os.environ['KMP_DUPLICATE_LIB_OK']='True'
import torch
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np


if torch.cuda.is_available():
    print('Cuda is available!')
else:
    print('Cuda is not available!')


#IMAGE_PATH = 'surf.jpeg'
IMAGE_PATH = 'Optimized-Tax.png'

reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH, rotation_info=[90, 180, 270], detail=1)
result
print(len(result))
print(result)
for x in range(0,len(result)):
    print(result[x][1])
# print(result[0][1],result[1][1],result[2][1])


text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread(IMAGE_PATH)
spacer = 100
for detection in result:
    top_left = tuple([int(detection[0][0][0]),int(detection[0][0][1])])
    bottom_right = tuple([int(detection[0][2][0]),int(detection[0][2][1])])
    text = detection[1]
    img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
    img = cv2.putText(img, text, top_left, font, 2, (255, 0, 0), 3, cv2.LINE_AA)
    spacer += 10

plt.imshow(img)
plt.show()
