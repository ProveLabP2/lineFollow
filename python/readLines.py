import cv2
import matplotlib
import pyCV
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt
import matplotlib.animation as animation

cap = cv2.VideoCapture(1)
ret, frame = cap.read()
fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), animated=True)
def updatefig(*args):
    ret, frame = cap.read()
    frame = pyCV.line_image(frame)
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    return im
ani = animation.FuncAnimation(fig, updatefig, interval=1)
plt.show()


