from threading import Thread
import cv2, time
import numpy as np

# Frame Size
width = 1920
height = 1080

# RED
lowRed_HSV1 = np.array([0, 70, 50])
highRed_HSV1 = np.array([10, 255, 255])
lowRed_HSV2 = np.array([170, 70, 50])
highRed_HSV2 = np.array([180, 255, 255])


class VideoStreamWidget(object):
    print('hahahah')
    def __init__(self, src=0):
        self.frame = None
        self.capture = cv2.VideoCapture(src)
        self.capture.set(3, width)
        self.capture.set(4, height)
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                start_time = time.time()
                (self.status, self.frame) = self.capture.read()
                blurredFrame = cv2.GaussianBlur(self.frame, (5, 5), 0)
                hsvFrame = cv2.cvtColor(blurredFrame, cv2.COLOR_BGR2HSV)
                red_mask1 = cv2.inRange(hsvFrame, lowRed_HSV1, highRed_HSV1)
                red_mask2 = cv2.inRange(hsvFrame, lowRed_HSV2, highRed_HSV2)

                redFrame = cv2.bitwise_and(self.frame, self.frame, mask=red_mask1)
                red_mask = red_mask1 | red_mask2
                contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
                for contour in contours:
                    if cv2.contourArea(contour) > 1000:
                        x, y, w, h = cv2.boundingRect(contour)
                        cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                FPS = int(1.0 / (time.time() - start_time))
                self.frame = cv2.putText(self.frame, f'FPS: {FPS}', [width - 120, 30], cv2.FONT_HERSHEY_SIMPLEX, 1,
                                         (0, 0, 255), 2, cv2.LINE_AA)
            time.sleep(.01)

    def show_frame(self):
        # Display frames in main program
        cv2.imshow('frame', self.frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)


if __name__ == '__main__':
    video_stream_widget = VideoStreamWidget()

    while True:
        try:
            video_stream_widget.show_frame()
        except AttributeError:
            pass
