import cv2
import numpy as np

video = cv2.VideoCapture(0)
prevFrame = video.read()[1]
currFrame = video.read()[1]

run = False

while video.isOpened():
    currFrame = video.read()[1]
    norm = video.read()[1]

    grayscale = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (5,5), cv2.BORDER_DEFAULT)
    thresh = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)[1]
    
    if(run):
        diff = cv2.absdiff(thresh, prevFrame)
        contours = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        
        if contours:
            largestcontour = max(contours, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(largestcontour)
            if(cv2.contourArea(largestcontour) > 200):
                cv2.rectangle(currFrame, (x,y), (x+w, y+h), (0,255,0), 3)   

        cv2.imshow('output', currFrame)

    prevFrame = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)[1]
    run = True
    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

video.release()