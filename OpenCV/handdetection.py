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

    return tuple([((xt+xb)/2), ((yt+yb)/2)])

def showHands():
    count = 0
    if results.multi_hand_landmarks:                                                        #This loop of code simply constructs the hand that the mediapipe library will recognize.
        for hand_landmarks in results.multi_hand_landmarks:
            for  lm in hand_landmarks.landmark:
                height, width, channel = currFrame.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                
                list.append(tuple([cx, cy]))                                                #This line of code will add all of the joints' x and y coordiantes to a list. 
                                                                                            #Each index number of the list will correspond to the the joint number 
                                                                                            #shown in the image on the slides. 

            #mp_draw.draw_landmarks(currFrame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if(len(list) >= 20):
        edgepoints = [list[4],list[8],list[12],list[16],list[20]]                           #i will be looping through all of the finger tip positions

        for i in edgepoints:

            threshold = distance(findPalm(list[0], list[9]), list[9]) * 1.5                 #finding the threshold (solution to the constant problem)
            #cv2.circle(currFrame, (int(x),int(y)), 5,(255, 255, 255), 2)
            if(distance(i, findPalm(list[0], list[9])) > threshold):                        #if the distance of a particular hand tip is above the threshold, add 1 to a "count" 
                                                                                            #variable. The maximum this can ever be is 5.
                count = count + 1

    if(len(list) > 20):                                                                     #i want to reset the list of hand joints every frame, since they change all the time
        list.clear()

    cv2.rectangle(currFrame, (25,50), (100, 150), (255, 255, 255), -1)                      #display stuff
    cv2.putText(currFrame, str(count), (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3, cv2.LINE_AA)


while video.isOpened():                                                                     #the following code simply runs the code we talked about
    ret, currFrame = video.read()

    imgRGB = cv2.cvtColor(currFrame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    showHands()

    s = 2

    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("output", 640*s, 480*s)
    cv2.imshow('output', currFrame)

    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

    prevFrame = currFrame
    ret, prevFrame = video.read()

video.release()