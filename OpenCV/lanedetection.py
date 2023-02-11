import cv2
import numpy as np

video = cv2.VideoCapture(r'C:\github\PythonProjects\OpenCV\roadvid.mp4')

delay = 30
l = 0
r = 0
slLeft = 0
slRight = 0
y_intL = 0
y_intR = 0

while video.isOpened():
    ret, vid = video.read()
    gray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    vertices = np.array([[(0, vid.shape[0]-250), (0, 0), (vid.shape[1],0), (vid.shape[1], vid.shape[0]), (vid.shape[1]-150, vid.shape[0]), (vid.shape[1]-790, 570), (860,570)]], dtype=np.int32)
    lowWhite = np.array([210,210,210])
    highWhite = np.array([255,255,255])
    mask = cv2.inRange(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB), lowWhite, highWhite)
    cv2.fillPoly(mask, vertices, (0,0,0))
    edges = cv2.Canny(mask, 100,200)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(edges, kernel, iterations=1)
    lines = cv2.HoughLinesP(dilation, 1, np.pi/180, 100, 20, 10)

    if(delay == 30):
        l = 0
        r = 0
        slLeft = 0
        slRight = 0
        y_intL = 0
        y_intR = 0
        
        for line in lines:
            x1, y1, x2, y2 = line[0]

            lineInfo = np.polyfit((x1, x2), (y1, y2), 1)
            slope = lineInfo[0]
            y_int = lineInfo[1]

            if slope < 0:
                l = l + 1
                slLeft = slLeft + slope
                y_intL = y_intL + y_int
            else:
                r = r + 1
                slRight = slRight + slope
                y_intR = y_intR + y_int

        if(l != 0):
            slLeft = slLeft/l
            y_intL = y_intL / l
        if(r != 0):
            slRight = slRight/r
            y_intR = y_intR / r 
        
        delay = 0

    if(len(lines) > 0): 
        xPos1=0
        xPos2=0

        #y − y1 = m(x − x1)

        if(l != 0):
            xPos1 = int((600-y_intL)/slLeft)
            cv2.line(vid, (0,int(y_intL)), (xPos1, 600), (0,0,0), 5)
        if(r != 0):        
            xPos2 = int((600-y_intR)/slRight)
            cv2.line(vid , (int(xPos2 + (vid.shape[0]-600)*slRight), vid.shape[0]), (xPos2, 600), (0,0,0), 5)

        vertices = np.array([[(vid.shape[1], vid.shape[0]), (0,int(y_intL)), (xPos1, 600), (xPos2, 600), (int(xPos2 + (vid.shape[0]-600)*slRight), vid.shape[0])]], dtype=np.int32)
        cv2.fillPoly(vid, vertices, (0,255,0))

    cv2.imshow("result", vid)
    
    delay = delay  + 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break