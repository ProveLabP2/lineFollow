#!/usr/bin/python3
import cv2
import matplotlib
import pyCV
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
    ret, frame = cap.read()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ax.imshow(cv2.cvtColor(frame[:, :], cv2.COLOR_BGR2RGB), animated=True)
    def updatefig(*args):
        ret, frame = cap.read()
        if len(argv) == 1:
            frame = pyCV.line_image(frame)
        else:
            frame = pyCV.line_image(frame,
                                    config['OPTIONS']['canny_threshold1'],
                                    config['OPTIONS']['canny_threshold2'],
                                    config['OPTIONS']['hough_threshold'],
                                    config['OPTIONS']['min_line_length'],
                                    config['OPTIONS']['max_gap'],
                                    config['OPTIONS']['rho'],
                                    config['OPTIONS']['theta'])
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        return im
    ani = animation.FuncAnimation(fig, updatefig, interval=1)
    plt.show()

if __name__ == "__main__":
    main(sys.argv)

