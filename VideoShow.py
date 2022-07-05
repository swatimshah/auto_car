from threading import Thread
import cv2
import time

class VideoShow:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:

            scale_percent = 35 # percent of original size
            width = int(self.frame.shape[1] * scale_percent / 100)
            height = int(self.frame.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized = cv2.resize(self.frame, dim, interpolation = cv2.INTER_AREA)

            print("show - start", round(time.time(), 3))  	
            cv2.imshow("Video", resized)
            print("show - end", round(time.time(), 3))  

            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True