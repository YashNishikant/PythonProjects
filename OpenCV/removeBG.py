import cv2;
import numpy as np;
from PIL import Image;

#precision can be changed here (0-1)
precision = 1

def whiteRange(dataint, acceptedval):
    precisionscaled = precision*80

    if precisionscaled > 80:
        precisionscaled = 80

    midvalue = acceptedval - precisionscaled
    if(midvalue + precisionscaled >= dataint >= midvalue - precisionscaled):
        return True
    return False

def checkBG(data):
    if(whiteRange(data[0],255) and whiteRange(data[1],255) and whiteRange(data[2],255)):
        return True
    return False

originalrgba = Image.open(r"C:\Users\yash0\sign.jpg")
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