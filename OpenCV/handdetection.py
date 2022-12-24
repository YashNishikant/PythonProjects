import cv2
import numpy as np
import mediapipe as mp
import math

video = cv2.VideoCapture(0)
ret, prevFrame = video.read()
ret, currFrame = video.read()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

list = []

def distance(pos1,pos2):
    x,y = pos1
    x1,y1 = pos2
    return math.sqrt(pow((x1-x),2) + pow((y1-y),2))

def findPalm(postop, posbottom):
    xt, yt = postop
    xb, yb = posbottom

    return tuple([xb, ((yt+yb)/2)])

def showHands():
    count = 0
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for  lm in hand_landmarks.landmark:
                height, width, channel = currFrame.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                #cv2.circle(currFrame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                
                list.append(tuple([cx, cy]))

            #mp_draw.draw_landmarks(currFrame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if(len(list) >= 20):
        edgepoints = [list[4],list[8],list[12],list[16],list[20]]

        for i in edgepoints:
            if(distance(i, findPalm(list[0], list[9])) > 80):
                count = count + 1

    if(len(list) > 20):
        list.clear()

    cv2.putText(currFrame, str(count), (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3, cv2.LINE_AA)

while video.isOpened():
    ret, currFrame = video.read()

    imgRGB = cv2.cvtColor(currFrame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    showHands()

    cv2.imshow('output', currFrame)

    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

    prevFrame = currFrame
    ret, prevFrame = video.read()

video.release()