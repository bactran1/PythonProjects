#Add Git PAT token

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import numpy as np

#this is just a test

#import Camera Iphone IP CAM URL
ipCam = 'rtsp://Bacs-iPhone.local:8554/live'

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        lowRed_HSV1 = np.array([0, 100, 20])
        highRed_HSV1 = np.array([10, 255, 255])
        lowRed_HSV2 = np.array([170, 100, 20])
        highRed_HSV2 = np.array([180, 255, 255])
        Capture = cv2.VideoCapture(0)
        # Capture = cv2.VideoCapture(ipCam)
        width = 1280
        height = 720
        Capture.set(3, width)
        Capture.set(4, height)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
                blurredFrame = cv2.GaussianBlur(frame, (7, 7), 0)
                hsvFrame = cv2.cvtColor(blurredFrame, cv2.COLOR_BGR2HSV)
                red_mask1 = cv2.inRange(hsvFrame, lowRed_HSV1, highRed_HSV1)
                red_mask2 = cv2.inRange(hsvFrame, lowRed_HSV2, highRed_HSV2)
                red_mask = red_mask1 | red_mask2
                redFrame = cv2.bitwise_and(frame, frame, mask=red_mask)
                contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
                for contour in contours:
                    if cv2.contourArea(contour) > 4000:
                        x, y, w, h = cv2.boundingRect(contour)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(width, height, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())