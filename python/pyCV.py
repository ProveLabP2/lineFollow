import os
import cv2
import numpy as np
import random
import math

import matplotlib
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt
#%matplotlib inline

def show_imgs(img_arr, cmap=None):
    fig, ax = plt.subplots(1, img_arr.shape[0], figsize=(15, 6),
        subplot_kw={'adjustable': 'box-forced'})
    axoff = np.vectorize(lambda ax:ax.axis('off'))
    axoff(ax)

    for i, img in enumerate(img_arr):
        ax[i].imshow(img, cmap=cmap)


def calc_points(x1, y1, slope):
    if slope == 0:
        return x1, 0
    else:
       return int(x1 - y1/slope) , 0

#fix TODO
def line_image(image, canny_threshold1=0, canny_threshold2=0,
        hough_threshold=2, min_line_length=3, max_gap=5, rho=2.0, theta=.3):

    #Read images, flip them vertically, and convert them to RGB color order
    #img_all = np.array(cv2.cvtColor(cv2.imread(images), cv2.COLOR_BGR2RGB))
    img = np.array(image[582:, :])
    #print(img_all[:, :, :] > [100, 0, 0])
    #img_all = img_all[:, :] > [125, 125, 125]
    #img_all = img_all[:, :, :] - 100
    #img_all = np.array([img[:, :] for img in img_all])
    #new_img = list(img_all[0])
    #print('ALL: ', img_all[0])
    #for i1, v1 in enumerate(new_img):
    #    for i2, v2 in enumerate(v1):
            #print(pixel)
    #        if (v2[1] < 125 and v2[2] < 125) or v2[0] > 100:
    #            new_img[i1][i2] = [0, 0, 0]
            #pass
    #new_img = np.array([new_img])
    #print('NEW: ', new_img[0])
    #return new_img[0]

    #find image dimensions
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([0, 100, 100])
    upper_yellow = np.array([70, 255, 255])
    #upper_yellow = np.array([70, 100, 100])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(img, img, mask=mask)
    gray_arr = np.array(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY))

    #blur images to avoid recognizing small lines
    blur_arr = np.array(cv2.blur(gray_arr,(1,1)))
    #imshow(blur_arr[0])
    #return blur_arr[0]
    #blur_arr = gray_arr
    #use canny threshold to find edges of shapes

    canny_arr = np.array(cv2.Canny(blur_arr, canny_threshold1, canny_threshold2))

    #return cv2.cvtColor(canny_arr,cv2.COLOR_GRAY2RGB)
    line_arr = []
    line_coord_arr = []
    line_count = 0
    lines = cv2.HoughLinesP(canny_arr, rho, theta, hough_threshold,
        min_line_length, max_gap)
    if lines is not None:
        h = len(img)
        w = len(img[0])
        minX, minY, maxX, maxY = lines[0][0]
        lines = np.array(lines).reshape(-1, 4)
        #print(lines)
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
                #cv2.line(img, (x1,y1),(x2,y2),(255,0,255),2)
            line_count += 1
        cv2.line(img, (minX,minY),(maxX,maxY),(0,255,0),2)
        slopeY = (maxY-minY)
        slopeX = (maxX-minX)
        slope = slopeY/slopeX
        #cv2.line(img, (w//2,h),(int((w//2) - slopeX),int (h - slopeY)),(0,0,255),2)
        lineX2 = w//2
        if slope != 0 and not math.isnan(slope):
            lineX2 = int((minX - minY/slope))
        cv2.line(img, (w//2,h),(lineX2,0),(0,0,255),2)
        value = (lineX2 - w/2)/w
        print(value)

    return img
