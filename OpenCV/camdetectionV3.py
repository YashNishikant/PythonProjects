import cv2
import numpy as np
import math
import pyautogui as pg
import time

video = cv2.VideoCapture(0)
prevFrame = video.read()[1]
currFrame = video.read()[1]

prevContours = []
currContours = []

tick = 0
x = 0
deltaX = 0
t1 = 0
t2 = 0
timepassed = 0
futuretime = 0

run = False
cooldown = False

def distance(x,y,x1,y1):
    return math.sqrt(pow((x1-x),2) + pow((y1-y),2))

while video.isOpened():
    
    t1 = time.time()
    timepassed = timepassed + (t1-t2)

    boxx = x
    
    tick = tick+1
    currFrame = video.read()[1]
    norm = video.read()[1]

    grayscale = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (5,5), cv2.BORDER_DEFAULT)
    thresh = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)[1]
    
    if(run):
        diff = cv2.absdiff(thresh, prevFrame)
        contours = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        
        i=len(contours)-1
        for c in contours:
            if(cv2.contourArea(contours[i]) < 100):
                contours = np.delete(contours, i, axis=0)
            i=i-1

        currContours = contours

        if len(contours) >= 1:
            x,y,w,h = cv2.boundingRect(contours[0])
            x = x 

            if len(prevContours) > 0: 
                deltaX = abs(boxx - x)
            else:
                deltaX = 0
            
            if len(contours) >= 2:
                x2,y2,w2,h2 = cv2.boundingRect(contours[1])

            if(cv2.contourArea(contours[0]) > 100):
                cv2.rectangle(currFrame, (x,y), (x+w, y+h), (0,255,0), 3)   

        if len(contours) >= 2 and distance(x,y,x2,y2) > 90:
            if(cv2.contourArea(contours[1]) > 100):
                cv2.rectangle(currFrame, (x2,y2), (x2+w2, y2+h2), (0,255,0), 3)   
                cv2.line(currFrame, (int(x+w/2),int(y+h/2)), (int(x2+w2/2),int(y2+h2/2)), (255,0,0), 3)
        if(deltaX > 200 and not cooldown):
            pg.moveTo(163,1066)
            pg.leftClick()
            time.sleep(1)
            pg.moveTo(1012, 342)
            pg.typewrite("https://github.com/YashNishikant")
            pg.press("enter")
            cooldown = True
            futuretime = timepassed + 10

        if timepassed > futuretime:
            cooldown = False
        else:
            cv2.putText(currFrame, str(int(futuretime-timepassed)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 2, cv2.LINE_AA)

    cv2.imshow('output', currFrame)

    prevFrame = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)[1]    
    
    if(run):
        prevContours = contours

    run = True
    
    t2 = t1
    
    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

video.release()