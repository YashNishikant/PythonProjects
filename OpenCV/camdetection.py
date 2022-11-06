import cv2
import numpy as np

time_2 = 0
video = cv2.VideoCapture(0)
ret, prevFrame = video.read()
overlap_image = np.zeros((720, 1280), dtype=np.uint8)
movement = np.zeros((720,1280), dtype=np.uint8)
brightness = np.zeros((720,1280), dtype=np.uint8)


while True:
    
    ret, currFrame = video.read()

    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

    movement = cv2.absdiff(currFrame, prevFrame)
        
    prevFrame = currFrame
    gray = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    test = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

    _, movementthresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    _, brightness = cv2.threshold(test, 127, 255, cv2.THRESH_BINARY)

    print("movement " + str(type(movementthresh)))
    print("brightness" + str(type(brightness)))

    cv2.bitwise_and(movementthresh, brightness, overlap_image)
    cv2.imshow('frame', overlap_image)



#one image is brightness and one image is movement  
#convert images to binary
#bitwise and
#find overlap
#np.unoit8
