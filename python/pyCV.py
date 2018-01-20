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

#fix TODO
def line_image(image, canny_threshold1=100, canny_threshold2=130,
        hough_threshold=2, min_line_length=3, max_gap=5, rho=2.0, theta=.3):
    images = image

    #Read images, flip them vertically, and convert them to RGB color order
    #img_all = np.array(cv2.cvtColor(cv2.imread(images), cv2.COLOR_BGR2RGB))
    img_all = np.array([image])

    #find image dimensions

    gray_arr = np.array([cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in img_all])

    #blur images to avoid recognizing small lines
    blur_arr = np.array([cv2.blur(arr,(5,5)) for arr in gray_arr])
    #blur_arr = gray_arr
    #use canny threshold to find edges of shapes
    canny_threshold1 = 100
    canny_threshold2 = 130

    canny_arr = np.array([cv2.Canny(arr, canny_threshold1, canny_threshold2) for arr in blur_arr])
    hough_threshold = 2
    min_line_length = 3
    max_gap = 5
    rho = 2.0
    theta = .3

    line_arr = []
    line_coord_arr = []
    line_count = 0
    for i, canny in enumerate(canny_arr):
        lines = cv2.HoughLinesP(canny, rho, theta, hough_threshold, min_line_length,
            max_gap)
        img = img_all[i]
        if lines is not None:
            minX, minY, maxX, maxY = lines[0][0]
            for line in lines:
                x1, y1, x2, y2 = line[0]
                if y1 < minY:
                    minY = y1
                    minX = x1
                if y2 < minY:
                    minY = y2
                    minX = x2
                if y1 > maxY:
                    maxY = y1
                    maxX = x1
                if y2 > maxY:
                    maxY = y2
                    maxX = x2
                line_coord = np.array([[[x1, y1], [x2, y2]]], dtype=float)
                cv2.line(img, (x1,y1),(x2,y2),(255,0,255),2)
                line_count += 1
            cv2.line(img, (minX,minY),(maxX,maxY),(0,255,0),2)
        line_arr.append(img)
    line_arr = np.array(line_arr)

    return img
