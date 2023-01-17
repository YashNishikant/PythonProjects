import cv2
import numpy as np
from  PIL import Image

#C:\Users\yash0\prayge.jpg

video = cv2.VideoCapture(r'C:\github\PythonProjects\OpenCV\roadvid.mp4')

while video.isOpened():

    ret, vid = video.read()

    gray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(gray, 50, 200)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, 20, 10)


    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(vid, (x1, y1), (x2, y2), (255,0,0), 3)

    cv2.imshow("result", vid)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break