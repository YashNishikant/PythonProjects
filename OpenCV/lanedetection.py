import cv2
import numpy as np
from  PIL import Image
import sys
import math

#C:\Users\yash0\prayge.jpg

img = cv2.imread(r'C:\Users\yash0\prayge.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 200)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, 10, 250)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255,0,0), 3)

cv2.imshow("Result", img)