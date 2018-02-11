#!/usr/bin/python3
import cv2
import matplotlib
import pyCV2
import sys
import configparser
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt
import matplotlib.animation as animation


def main(argv):
    config = []
    if len(argv) > 1:
        config = configparser.ConfigParser()
        config.read(argv[1])
    cap = cv2.VideoCapture('../images/GP015331.MP4')
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

    while(True):
        angle = updatefig()
        print("ANGLE GIVEN: " , angle)


if __name__ == "__main__":
    main(sys.argv)

