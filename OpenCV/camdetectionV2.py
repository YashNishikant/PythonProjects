import cv2
import numpy as np

video = cv2.VideoCapture(0)
ret, prevFrame = video.read()
ret, currFrame = video.read()

while True:
    ret, currFrame = video.read()

    diff = cv2.absdiff(currFrame, prevFrame)
    grayscale = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (5,5),0)
    ret, thresh = cv2.threshold(blur, 20, 255, 0, cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh,np.ones((3,3),np.uint8), iterations=3)
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        if(cv2.contourArea(c) > 1000):
            print(cv2.contourArea(c))
            cv2.drawContours(currFrame, contours, -1, (0,255,0), 2)


    cv2.imshow('output', currFrame)

    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break
    prevFrame = currFrame
    ret, prevFrame = video.read()

video.release()