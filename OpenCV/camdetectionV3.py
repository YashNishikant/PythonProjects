import cv2
import numpy as np
import math

video = cv2.VideoCapture(0)
prevFrame = video.read()[1]
currFrame = video.read()[1]

run = False

def distance(x,y,x1,y1):
    return math.sqrt(pow((x1-x),2) + pow((y1-y),2))

while video.isOpened():
    currFrame = video.read()[1]
    norm = video.read()[1]

    grayscale = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (5,5), cv2.BORDER_DEFAULT)
    thresh = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)[1]
    
    if(run):
        diff = cv2.absdiff(thresh, prevFrame)
        contours = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        print(contours)
        if len(contours) >= 2:
    
            x,y,w,h = cv2.boundingRect(contours[0])
            x2,y2,w2,h2 = cv2.boundingRect(contours[1])

            if(cv2.contourArea(contours[0]) > 100):
                cv2.rectangle(currFrame, (x,y), (x+w, y+h), (0,255,0), 3)   

            if(cv2.contourArea(contours[1]) > 100):
                cv2.rectangle(currFrame, (x2,y2), (x2+w2, y2+h2), (0,255,0), 3)   

            print(distance(x,x2,y,y2))

        cv2.imshow('output', currFrame)

    prevFrame = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)[1]
    run = True
    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

video.release()