from threading import Thread
import cv2
import time

class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):    
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                print("read - start", round(time.time(), 3))  	
                (self.grabbed, self.frame) = self.stream.read()
                print("read - end", round(time.time(), 3))  	

    def stop(self):
        self.stopped = True