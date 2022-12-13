import cv2
import numpy as np
from  PIL import Image
import sys
import math

#C:\Users\yash0\prayge.jpg
    
src = cv2.imread("prayge.jpg", cv2.IMREAD_GRAYSCALE)
dst = cv2.Canny(src, 50, 200, None, 3)
lines = cv2.HoughLines(dst, 1, np.pi/180, 150, None, 0,0)
cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)


if lines:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv2.line(cdst, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
