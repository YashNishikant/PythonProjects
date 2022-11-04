import cv2
import numpy as np

time_2 = 0
video = cv2.VideoCapture(0)
ret, prevFrame = video.read()

while True:
    
    ret, currFrame = video.read()

    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break


    movement = cv2.absdiff(currFrame, prevFrame)
        
    prevFrame = currFrame
    gray = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)

    brightness = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('frame', movement)



#one image is brightness and one image is movement  
#convert images to binary
#bitwise and
#find overlap