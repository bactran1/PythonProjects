from threading import Thread

import cv2
import numpy as np
import time

# Frame Size
width = 1280
height = 720

# RED
lowRed_HSV1 = np.array([0, 70, 50])
highRed_HSV1 = np.array([10, 255, 255])
lowRed_HSV2 = np.array([170, 70, 50])
highRed_HSV2 = np.array([180, 255, 255])


# defining a helper class for implementing multi-threading
class WebcamStream:
    # initialization method
    def __init__(self, stream_id=0):
        self.stream_id = stream_id  # default is 0 for main camera

        # opening video capture stream
        self.cap = cv2.VideoCapture(self.stream_id)
        self.cap.set(3, width)
        self.cap.set(4, height)
        if self.cap.isOpened() is False:
            print("[Exiting]: Error accessing webcam stream.")
            exit(0)
        #fps_input_stream = int(self.cap.get(5))  # hardware fps
        #print(f"FPS of input stream: {fps_input_stream}")

        # reading a single frame from vcap stream for initializing
        self.grabbed, self.frame = self.cap.read()
        if self.grabbed is False:
            print('[Exiting] No more frames to read')
            exit(0)
        # self.stopped is initialized to False
        self.stopped = True
        # thread instantiation
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True  # daemon threads run in background

    # method to start thread
    def start(self):
        self.stopped = False
        self.t.start()

    # method passed to thread to read next available frame
    def update(self):
        while True:
            if self.stopped is True:
                break
            self.grabbed, self.frame = self.cap.read()
            if self.grabbed is False:
                print('[Exiting] No more frames to read')
                self.stopped = True
                break
        self.cap.release()

    # method to return latest read frame
    def read(self):
        return self.frame

    # method to stop reading frames
    def stop(self):
        self.stopped = True


# initializing and starting multi-threaded webcam input stream
webcam_stream = WebcamStream(stream_id=0)  # 0 id for main camera
webcam_stream.start()
# processing frames in input stream

while True:
    if webcam_stream.stopped is True:
        break
    else:
        start_time = time.time()
        frame = webcam_stream.read()
        blurredFrame = cv2.GaussianBlur(frame, (7, 7), 0)
        hsvFrame = cv2.cvtColor(blurredFrame, cv2.COLOR_BGR2HSV)
        red_mask1 = cv2.inRange(hsvFrame, lowRed_HSV1, highRed_HSV1)
        red_mask2 = cv2.inRange(hsvFrame, lowRed_HSV2, highRed_HSV2)

        redFrame = cv2.bitwise_and(frame, frame, mask=red_mask1)
        red_mask = red_mask1 | red_mask2
        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            if cv2.contourArea(contour) > 5000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        FPS = int(1.0 / (time.time() - start_time))
        frame = cv2.putText(frame, f'FPS: {FPS}', [width - 120, 30], cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2, cv2.LINE_AA)
    # adding a delay for simulating video processing time
    delay = 0.03  # delay value in seconds

    # displaying frame
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
webcam_stream.stop()  # stop the webcam stream

# printing time elapsed and fps

# closing all windows
cv2.destroyAllWindows()
