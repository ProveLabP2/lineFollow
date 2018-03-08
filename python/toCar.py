#!/usr/bin/python3
import cv2
import pyCV2
import time
import sys
import configparser
import serial
from picamera.array import PiRGBArray
from picamera import PiCamera

def main(argv):
   # ser = serial.Serial(
   #     port='/dev/ttyUSB0',
   #     baudrate=9600
   # )
    config = []
    if len(argv) > 1:
        config = configparser.ConfigParser()
        config.read(argv[1])
    camera = PiCamera()
    camera.resolution=(1920, 1088)
    rawCapture = PiRGBArray(camera, size = (1920, 1088))
    time.sleep(.1)
    #cap = cv2.VideoCapture('../images/GP015331.MP4')
    def updatefig(*args):
        ret, frame = rawCapture.read()
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

    print("___");
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        print("---");
        image = frame.array
        angle = pyCV2.line_image(image)
        print("___");
        angle += 1
        print("ANGLE GIVEN: " , angle)
        #ser.write(str(angle).encode())
        print("ANGLE SENT")
        rawCapture.truncate(0)

if __name__ == "__main__":
    main(sys.argv)

