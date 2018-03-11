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
def line_image(image, canny_threshold1=80, canny_threshold2=150,
        hough_threshold=30, min_line_length=3, max_gap=5, rho=2.0, theta=.3):

    #Read images, flip them vertically, and convert them to RGB color order
    img = np.array(image[:, :])
    scale = .5
    new_img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR) 
    hsv = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([0, 100, 100])
    upper_yellow = np.array([70, 255, 255])
    lower_blue = np.array([90, 0, 0])
    upper_blue = np.array([120, 255, 150])
    lower_green = np.array([50, 0, 0])
    upper_green = np.array([80, 255, 100])
    #return new_img

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(new_img, new_img, mask=mask)
    gray_arr = np.array(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY))
    #return res

    #blur images to avoid recognizing small lines
    blur_arr = np.array(cv2.blur(gray_arr,(1,5)))
    #use canny threshold to find edges of shapes
    v = np.median(blur_arr)
    sigma = .33

    #---- apply automatic Canny edge detection using the computed median----
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    #print(lower, '   ', upper)

    #canny_arr = np.array(cv2.Canny(blur_arr, canny_threshold1, canny_threshold2))
    canny_arr = np.array(cv2.Canny(blur_arr, 100, 150))
    #return cv2.cvtColor(canny_arr, cv2.COLOR_GRAY2RGB)

    line_arr = []
    line_coord_arr = []
    line_count = 0
    lines = cv2.HoughLinesP(canny_arr, rho, theta, hough_threshold)
    value = 0
    h = len(img)
    w = len(img[0])
    topIntercept = w//2
    botIntercept = w//2
    if lines is not None:
        minX, minY, maxX, maxY = lines[0][0]
        lines = np.array(lines).reshape(-1, 4)
        for line in lines:
            x1, y1, x2, y2 = line
            if y1 > minY:
                minY = y1
                minX = x1
            if y2 > minY:
                minY = y2
                minX = x2
            if y1 < maxY:
                maxY = y1
                maxX = x1
            if y2 < maxY:
                maxY = y2
                maxX = x2
            line_count += 1
            #cv2.line(img, (int(x1/scale), int(y1/scale)), (int(x2/scale), int(y2/scale)), (0, 0, 255), 5)
        maxX = int(maxX/scale)
        minX = int(minX/scale)
        maxY = int(maxY/scale)
        minY = int(minY/scale)
        slopeY = (maxY-minY)
        slopeX = (maxX-minX)
        #cv2.line(img, (maxX, maxY), (minX, minY), (0, 255, 0), 5)
        if slopeX == 0:
            botIntercept = maxX
            topIntercept = maxX
            slope = 'no'
        else:
            slope = slopeY/slopeX
            yInt = (maxY - slope*maxX)
            if slope != 0 and not math.isnan(slope):
                topIntercept = (-1*yInt/slope)
                botIntercept = (h - yInt)/slope
            else:
                value = 0
        #cv2.line(img, (int(topIntercept), 0), (int(botIntercept), h), (255, 0, 0), 3)
    botDiff = botIntercept - w//2
    topDiff = topIntercept - w//2
    if abs(botDiff) > .10*w:
        value = botDiff/w
    else:
        value = topDiff/w
    if value > 1:
        value = 1
    elif value < -1:
        value =  -1
    return value
