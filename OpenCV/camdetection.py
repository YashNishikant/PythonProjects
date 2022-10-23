import cv2
import numpy as np

time_2 = 0
fps = 0
video = cv2.VideoCapture(0)
ret, prevFrame = video.read()
switch = False

while True:
    
    ret, currFrame = video.read()

    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

    if cv2.waitKey(1)  & 0xFF == ord('a'):
        switch = not switch

    if switch:
        movement = cv2.absdiff(currFrame, prevFrame)
        
        prevFrame = currFrame
        gray = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)

        brightness = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        lightDetection = cv2.bitwise_and(movement, brightness)

        cv2.imshow('frame', lightDetection)
    else:
        cv2.imshow('frame', currFrame)



#one image is brightness and one image is movement  
#convert images to binary
#bitwise and
#find overlap