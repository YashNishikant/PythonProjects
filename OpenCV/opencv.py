import cv2;
import numpy as np;
from PIL import Image;

def whiterange(data):

    if(data[0] == 255 and data[1] == 255 and data[2] == 255):
        return True
    return False


rgba = Image.open(r"C:\Users\yash0\Downloads\sig.jpg").convert("RGBA")
imagedata = rgba.getdata()
newdata = []

for d in imagedata:
    if(whiterange(d)):
        newdata.append((255,255,255,0))
    else:
        newdata.append(d)
     
print("done")

rgba.putdata(newdata)
rgba.save("newSig.png", "PNG")

