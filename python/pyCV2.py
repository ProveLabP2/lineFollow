import os
import cv2
import numpy as np
import random
import math

def calc_points(x1, y1, slope):
    if slope == 0:
        return x1, 0
    else:
       return int(x1 - y1/slope) , 0

#fix TODO
def line_image(image, canny_threshold1=0, canny_threshold2=0,
        hough_threshold=2, min_line_length=3, max_gap=5, rho=2.0, theta=.3):

    #Read images, flip them vertically, and convert them to RGB color order
    img = np.array(image[582:, :])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([0, 100, 100])
    upper_yellow = np.array([70, 255, 255])
    #upper_yellow = np.array([70, 100, 100])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(img, img, mask=mask)
    gray_arr = np.array(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY))

    #blur images to avoid recognizing small lines
    blur_arr = np.array(cv2.blur(gray_arr,(1,1)))
    #use canny threshold to find edges of shapes

    canny_arr = np.array(cv2.Canny(blur_arr, canny_threshold1, canny_threshold2))

    line_arr = []
    line_coord_arr = []
    line_count = 0
    lines = cv2.HoughLinesP(canny_arr, rho, theta, hough_threshold,
        min_line_length, max_gap)
    value = 0
    if lines is not None:
        h = len(img)
        w = len(img[0])
        minX, minY, maxX, maxY = lines[0][0]
        lines = np.array(lines).reshape(-1, 4)
        for line in lines:
            x1, y1, x2, y2 = line
            if(x1 > (w - (3.5*y1) - 1200) and (x1 < w - (1*y1) - 800) and
               x2 > (w - (3.5*y2) - 1200) and (x2 < w - (1*y2) - 800) and
               x2 < w/2 + 50 and y2 > 100):
                if y1 > minY or (y1 == minY and x1 > minX):
                    minY = y1
                    minX = x1
                if y2 > minY or (y2 == minY and x2 > minX):
                    minY = y2
                    minX = x2
                if x1 > maxX:
                    maxY = y1
                    maxX = x1
                if x2 > maxX:
                    maxY = y2
                    maxX = x2
            line_count += 1
        slopeY = (maxY-minY)
        slopeX = (maxX-minX)
        if slopeX == 0:
            value = 0
        else:
            slope = slopeY/slopeX
            lineX2 = w//2
            if slope != 0 and not math.isnan(slope):
                lineX2 = int((minX - minY/slope))
            value = (lineX2 - w/2)/w
    if value > 1:
        return 1
    elif value < -1:
        return -1
    else:
        return value
