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
def line_image(image, canny_threshold1=100, canny_threshold2=130,
        hough_threshold=2, min_line_length=3, max_gap=5, rho=2.0, theta=.3):

    #Read images, flip them vertically, and convert them to RGB color order
    #img_all = np.array(cv2.cvtColor(cv2.imread(images), cv2.COLOR_BGR2RGB))
    img = np.array(image[:, :])
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

    lower_yellow = np.array([0, 80, 80])
    upper_yellow = np.array([70, 255, 255])
    #upper_yellow = np.array([70, 100, 100])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(img, img, mask=mask)

    print(res)
    return res
    gray_arr = np.array(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

    #blur images to avoid recognizing small lines
    blur_arr = np.array(cv2.blur(gray_arr,(2,2)))
    #imshow(blur_arr[0])
    #return blur_arr[0]
    #blur_arr = gray_arr
    #use canny threshold to find edges of shapes
    canny_threshold1 = 100
    canny_threshold2 = 130

    canny_arr = np.array(cv2.Canny(blur_arr, canny_threshold1, canny_threshold2))
    hough_threshold = 2
    min_line_length = 3
    max_gap = 5
    rho = 2.0
    theta = .3

    line_arr = []
    line_coord_arr = []
    line_count = 0
    lines = cv2.HoughLinesP(canny_arr, rho, theta, hough_threshold,
        min_line_length, max_gap)
    if lines is not None:
        #minX, minY, maxX, maxY = lines[0][0]
        lines = np.array(lines).reshape(-1, 4)
        #print(lines)
        avg_slopes = np.mean((lines[:,3] - lines[:,1])/(lines[:,2] - lines[:,0]))
        avgX1, avgY1, avgX2, avgY2 = np.mean(lines, axis=0)
        avg2 = np.mean(lines[:,3] - lines[:, 1])/np.mean(lines[:,2] - lines[:, 0])
        print("S1: ", np.mean(avg_slopes[not math.isinf(avg_slopes)]))
        print("S2: ", avg2)
        print([avgX1, avgY1, avgX2, avgY2]) 
        avg_slope = (avgY2 - avgY1)/(avgX2 - avgX1)

        for line in lines:
            x1, y1, x2, y2 = line
            #if y1 < minY:
            #    minY = y1
            #    minX = x1
            #if y2 < minY:
            #    minY = y2
            #    minX = x2
            #if y1 > maxY:
            #    maxY = y1
            #    maxX = x1
            #if y2 > maxY:
            #    maxY = y2
            #    maxX = x2
            line_coord = np.array([[[x1, y1], [x2, y2]]], dtype=float)
            cv2.line(img, (x1,y1),(x2,y2),(255,0,255),2)
            line_count += 1
        #cv2.line(img, (minX,minY),(maxX,maxY),(0,255,0),2)
        slopedX1 = int(len(img[0])/2); slopedY1 = len(img)
        #slopedX2 = len(img); slopedY2 =  int(avg_slope*slopedX2)
        slopedX2, slopedY2 = calc_points(slopedX1, slopedY1, avg_slope)
        print(avg_slope)
        print(len(img), len(img[0]))
        print([slopedX1, slopedY1, slopedX2, slopedY2])
        #boo, (slopedX1, slopedY1), (slopedX2, slopedY2) = \
        #cv2.clipLine((0, 0, len(img), len(img[0])), (slopedX1, slopedY1), (slopedX2, slopedY2))
        cv2.line(img, (slopedX1, slopedY1), 
            (slopedX2, slopedY2), (255,0,255),2)
        #print(cv2.clipLine((0, 0, len(img[0]), len(img)), (slopedX1, slopedY1), (slopedX2, slopedY2)))
        print([slopedX1, slopedY1, slopedX2, slopedY2])

    return img
