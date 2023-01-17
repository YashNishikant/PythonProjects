import cv2
import numpy as np
import mediapipe as mp
import math
import pyautogui

video = cv2.VideoCapture(0)
ret, prevFrame = video.read()
ret, currFrame = video.read()

pyautogui.PAUSE = 0
previousMode = 0

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
                cv2.circle(currFrame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

                list.append(tuple([cx, cy]))

            mp_draw.draw_landmarks(currFrame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if(len(list) >= 20):
        edgepoints = [list[4],list[8],list[12],list[16],list[20]]

        for i in edgepoints:
            if(distance(i, findPalm(list[0], list[9])) > 60):
                count = count + 1

    if(len(list) > 20):
        list.clear()

    global previousMode
    if(count == 2):
        indexX = edgepoints[1]
        (x,y) = indexX


        #scale x from 0 to 640 to 1920

        screenResolution = pyautogui.size()

        screenX = screenResolution[0]
        screenY = screenResolution[1]


        x = int(x * (screenX/640))
        y = int(y * (screenY/480))

        pyautogui.moveTo(x, y)

    if(count == 3 and previousMode != 3):
        pyautogui.click()


    
    previousMode = count


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