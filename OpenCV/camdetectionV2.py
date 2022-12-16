import cv2
import numpy as np
import mediapipe as mp

video = cv2.VideoCapture(0)
ret, prevFrame = video.read()
ret, currFrame = video.read()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

togglehands = True

def showHands():
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for  lm in hand_landmarks.landmark:
                height, width, channel = currFrame.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                cv2.circle(currFrame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
            mp_draw.draw_landmarks(currFrame, hand_landmarks, mp_hands.HAND_CONNECTIONS)


while video.isOpened():
    ret, currFrame = video.read()

    imgRGB = cv2.cvtColor(currFrame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if togglehands:
        showHands()

    diff = cv2.absdiff(currFrame, prevFrame)
    grayscale = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (35,35),0)
    ret, thresh = cv2.threshold(blur, 20, 255, 0, cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh,np.ones((3,3),np.uint8), iterations=3)
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largestcontour = max(contours, key=cv2.contourArea)
        
        x,y,w,h = cv2.boundingRect(largestcontour)
        cv2.rectangle(currFrame, (x,y), (x+w, y+h), (0,255,0), 3)   
    else:
        cv2.drawContours(currFrame, contours, -1, (0,255,0), 2)

    cv2.imshow('output', currFrame)

    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

    if cv2.waitKey(1)  & 0xFF == ord('a'):
        togglehands = not togglehands

    prevFrame = currFrame
    ret, prevFrame = video.read()

video.release()