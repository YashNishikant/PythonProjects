import cv2;
import numpy as np;
from PIL import Image;

def whiteRange(dataint, acceptedval):
    if(acceptedval + 20 >= dataint >= acceptedval - 20):
        return True
    return False

def checkBG(data):
    if(whiteRange(data[0],235) and whiteRange(data[1],235) and whiteRange(data[2],235)):
        return True
    return False

originalrgba = Image.open(r"C:\Users\yash0\prayge.jpg")
rgba = originalrgba.convert("RGBA")
imagedata = rgba.getdata()
newdata = []

for d in imagedata:
    if(checkBG(d)):
        newdata.append((255,255,255,0))
    else:
        newdata.append(d)
        
rgba.putdata(newdata)

originalrgba.show()
rgba.show()