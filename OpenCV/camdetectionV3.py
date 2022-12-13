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

x = 0
deltaX = 0
t1 = 0
t2 = 0
timepassed = 0
futuretime = 0

run = False
cooldown = False

enableauto = False

def distance(x,y,x1,y1):
    return math.sqrt(pow((x1-x),2) + pow((y1-y),2))

while video.isOpened():
    
    #used for time passed
    t1 = time.time()
    #timepassed = timepassed + deltaTime
    timepassed = timepassed + (t1-t2)

    currFrame = video.read()[1]

    box_x = x

    #grayscaling, blurring, thresh
    grayscale = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (5,5), cv2.BORDER_DEFAULT)
    thresh = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)[1]
    
    #needs a "run" boolean because the first iteration of the loop needs to initialize values of the current frame and the previous frame
    #the code cannot run through the first iteration because values of the previous frame have not been initialized

    if(run):

        #displays value of a boolean that allows us to enable the automation code
        cv2.putText(currFrame, "Swipe Detection: " + str(enableauto), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv2.LINE_AA)

        #finds contours of the absdiff of our image
        diff = cv2.absdiff(thresh, prevFrame)
        contours = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

        #sort the contours so that the biggest two are in index 0 and 1
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        
        #checks if the contours found are big enough. if not, remove them from the contours list
        #small contours in the background that shouldn't be there can cause problems
        i=len(contours)-1
        for c in contours:
            if(cv2.contourArea(contours[i]) < 100):
                contours = np.delete(contours, i, axis=0)
            i=i-1

        currContours = contours

        #if there are contours in the list, draw the largest one
        if len(contours) >= 1:
            x,y,w,h = cv2.boundingRect(contours[0])

            #find the displacement in x between the previous frame and the current frame
            if len(prevContours) > 0: 
                deltaX = abs(box_x - x)
            
            #if there are no contours, there's no displacement
            else:
                deltaX = 0
            
            #if theres a SECOND light, draw a SECOND contour box
            if len(contours) >= 2:
                x2,y2,w2,h2 = cv2.boundingRect(contours[1])

            #draw a box around the first biggest contour
            if(cv2.contourArea(contours[0]) > 100):
                cv2.rectangle(currFrame, (x,y), (x+w, y+h), (0,255,0), 3)   

        #if two contours are far apart enough, draw a box around the second largest one and connect them with a line
        if len(contours) >= 2 and distance(x,y,x2,y2) > 120:
            if(cv2.contourArea(contours[1]) > 100):
                cv2.rectangle(currFrame, (x2,y2), (x2+w2, y2+h2), (0,255,0), 3)   
                cv2.line(currFrame, (int(x+w/2),int(y+h/2)), (int(x2+w2/2),int(y2+h2/2)), (255,0,0), 3)

        #if the horizontal displacement is over 200 pixels, use a python automated library to open up my github on chrome
        #there is also a cooldown i added so the code doesn't fire off when unintended
        print(deltaX)
        print(cooldown)
        print(enableauto)
        if(deltaX > 200 and not cooldown and enableauto):
            pg.moveTo(163,1066)
            pg.leftClick()
            time.sleep(1)
            pg.moveTo(1012, 342)
            pg.typewrite("https://github.com/YashNishikant")
            pg.press("enter")
            cooldown = True

            #cooldown is set to 10 seconds
            futuretime = timepassed + 10

        #when the cooldown is over, the cooldown boolean turns to false and if the cooldown is still active, display a counter
        if timepassed > futuretime:
            cooldown = False
        else:
            cv2.putText(currFrame, str(int(futuretime-timepassed)), (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)


    #display the current frame
    cv2.imshow('output', currFrame)

    #setting previous frame
    prevFrame = cv2.threshold(blur, 253, 255, cv2.THRESH_BINARY)[1]    
    
    #setting contours list of previous frame.
    #we are comparing the contour list between frames to avoid this bug:
        #whenever i first turned on a flashlight on the side of the screen with large x values, the code registers the action as a quick sweep. 
        #as a result, the pyautogui code would run when it wasn't supposed to
        #so im making sure of this: 
        #when the pyautogui code runs, there must have been a contour detected in the frame previous, 
        #meaning that i performed a quick sweep across the screen with the light, and i did not just turn on a light for the first time 
    if(run):
        prevContours = contours

    #allowing all my code to run after first loop iteration
    run = True
    
    #setting time passed of previous frame
    t2 = t1
    
    #press Q to quit application
    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

    #allowing pyautogui to function
    if cv2.waitKey(1)  & 0xFF == ord('a'):
        enableauto = not enableauto

video.release()