import cv2
import numpy as np

video = cv2.VideoCapture(1)
ret, prevFrame = video.read()
ret, currFrame = video.read()

while video.isOpened():
    ret, currFrame = video.read()

    diff = cv2.absdiff(currFrame, prevFrame)
    diffresult = cv2.multiply(diff, 10)

    grayscale = cv2.cvtColor(diffresult, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (5,5), cv2.BORDER_DEFAULT)
    ret, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow('output', diff)

    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

    prevFrame = currFrame
    ret, prevFrame = video.read()

video.release()