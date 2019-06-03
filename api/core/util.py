import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def getRGBImage(img, channel):
    return img.getchannel(channel)

def getHistogram(img):
    return img.histogram()
    
def cropImage(img, x1, y1, x2, y2):
    cropArea = (x1,y1,x2,y2)
    return img.crop(cropArea)

def sumArray(arr):
    return sum(arr)    

def showImage(red, green, blue):
    merge = Image.merge("RGB", (red, green, blue))
    merge.show()

def sumHistogram(red, green, blue):
    return sum(getHistogram(red)) + sum(getHistogram(red)) + sum(getHistogram(blue)) 

def executeChallenge(_img,_x1,_y1,_x2,_y2):
    
    img = Image.open("../challenge/imgs/" + _img)
    
    imCrop = cropImage(img, _x1, _y1, _x2, _y2)
    red = getRGBImage(imCrop, "R")
    green = getRGBImage(imCrop, "G")
    blue = getRGBImage(imCrop, "B")
   
    result = sumHistogram(red, green, blue)
    return result