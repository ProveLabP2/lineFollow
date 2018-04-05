#!/usr/bin/python3
import cv2
#import matplotlib
import pyCV2
import sys
import time
#import configparser
#from matplotlib.pyplot import imshow
#from matplotlib import pyplot as plt
#import matplotlib.animation as animation
from picamera.array import PiRGBArray
from picamera import PiCamera


def main(argv):
    #cap = cv2.VideoCapture('../images/20180220_152855.mp4')
    #cap = cv2.VideoCapture('../images/GP015331.MP4')
    camera = PiCamera()
    camera.resolution=(1920, 1088)
    rawCapture = PiRGBArray(camera, size = (1920, 1088))
    time.sleep(.1)
    #time.sleep(.1)
    #cap = cv2.VideoCapture(0)
    #ret, frame = cap.read()
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #im = ax.imshow(cv2.cvtColor(frame[:, 100:-100], cv2.COLOR_BGR2RGB), animated=True)
    '''
    def updatefig(*args):
        ret, frame = cap.read()
        frame = pyCV2.line_image(frame)
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        #im.set_array(frame)
        return im
    #while(True):
        #updatefig()
    #ani = animation.FuncAnimation(fig, updatefig, interval=1)
    #plt.show()
    '''
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        img = pyCV2.line_image(frame.array)
        cv2.imshow('image', img)
        cv2.waitKey(1)
        rawCapture.truncate(0)
        print(1)

if __name__ == "__main__":
    main(sys.argv)

