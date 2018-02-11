#!/usr/bin/python3
import cv2
import matplotlib
import pyCV2
import time
import sys
import configparser
from picamera.array import PiRGBArray
from picamera import PiCamera

def main(argv):
    config = []
    if len(argv) > 1:
        config = configparser.ConfigParser()
        config.read(argv[1])
    camera = PiCamera()
    capture = PiRGBArray(camera, size = (640, 480))
    time.sleep(.1)

    #cap = cv2.VideoCapture('../images/GP015331.MP4')
    def updatefig(*args):
        ret, frame = cap.read()
        angle = 0
        if len(argv) == 1:
            angle = pyCV2.line_image(frame)
        else:
            angle = pyCV2.line_image(frame,
                                    config['OPTIONS']['canny_threshold1'],
                                    config['OPTIONS']['canny_threshold2'],
                                    config['OPTIONS']['hough_threshold'],
                                    config['OPTIONS']['min_line_length'],
                                    config['OPTIONS']['max_gap'],
                                    config['OPTIONS']['rho'],
                                    config['OPTIONS']['theta'])
        return angle

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        angle = pyCV2.line_image(image)
        print("ANGLE GIVEN: " , angle)
        rawCapture.truncate(0)


if __name__ == "__main__":
    main(sys.argv)

