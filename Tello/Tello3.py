##############################################################################

import asyncio
import numpy as np
from threading import Thread

import cv2  # requires python-opencv 

from tello_asyncio import Tello, VIDEO_URL

print('[main thread] START')

##############################################################################
# drone control in worker thread 

def fly():
    print('[fly thread] START')
    async def main():
        drone = Tello()
        try:
            await asyncio.sleep(1)
            await drone.wifi_wait_for_network(prompt=True)
            await drone.connect()
            await drone.start_video(connect=False)
            await drone.takeoff()
            await drone.move_up(50)
            await drone.move_forward(250)
            await drone.turn_clockwise(20)
            await drone.turn_counterclockwise(40)
            await drone.turn_clockwise(20)
            await drone.turn_clockwise(180)
            await drone.move_forward(250)
            await drone.turn_clockwise(180)
            await drone.move_down(100)


            await drone.land()
        finally:
            await drone.stop_video()
            await drone.disconnect()

    # Python 3.7+
    #asyncio.run(main())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

    print('[fly thread] END')


fly_thread = Thread(target=fly, daemon=True)
fly_thread.start()

##############################################################################
# Video capture and GUI in main thread

print(f'[main thread] OpenCV capturing video from {VIDEO_URL}')
print(f'[main thread] Press Ctrl-C or any key with the OpenCV window focussed to exit (the OpenCV window may take some time to close)')

# RED
lowRed_HSV1 = np.array([0, 70, 50])
highRed_HSV1 = np.array([10, 255, 255])
lowRed_HSV2 = np.array([170, 70, 50])
highRed_HSV2 = np.array([180, 255, 255])

capture = None
try:
    capture = cv2.VideoCapture(VIDEO_URL)
    # capture.open(VIDEO_URL)

    while True:
        # grab and show video frame in OpenCV window
        grabbed, frame = capture.read()
        blurredFrame = cv2.GaussianBlur(frame, (7, 7), 0)
        hsvFrame = cv2.cvtColor(blurredFrame, cv2.COLOR_BGR2HSV)
        red_mask1 = cv2.inRange(hsvFrame, lowRed_HSV1, highRed_HSV1)
        red_mask2 = cv2.inRange(hsvFrame, lowRed_HSV2, highRed_HSV2)

        redFrame = cv2.bitwise_and(frame, frame, mask=red_mask1)
        red_mask = red_mask1 | red_mask2
        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            if cv2.contourArea(contour) > 2000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if grabbed:
            cv2.imshow('tello-asyncio', frame)

        # process OpenCV events and exit if any key is pressed    
        if cv2.waitKey(1) != -1:
            break
except KeyboardInterrupt:
    pass
finally:
    # tidy up
    if capture:
        capture.release()
    cv2.destroyAllWindows()

print('[main thread] END')
cv2.destroyAllWindows()