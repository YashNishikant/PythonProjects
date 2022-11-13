import cv2
import numpy as np

video = cv2.VideoCapture(1)
prevFrame = video.read()[1]
currFrame = video.read()[1]

run = False

diff = None

def drawContours():
    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    if contours:
        largestcontour = max(contours, key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(largestcontour)
        cv2.rectangle(currFrame, (x,y), (x+w, y+h), (0,255,0), 3)   

while video.isOpened():
    currFrame = video.read()[1]
    norm = video.read()[1]

    grayscale = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (5,5), cv2.BORDER_DEFAULT)
    thresh = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)[1]

    if run:
        diff = cv2.absdiff(thresh, prevFrame)
        cv2.imshow('output', currFrame)

    drawContours()

    prevFrame = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)[1]

    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

    run = True

video.release()