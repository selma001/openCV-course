import cv2 as cv
import numpy as np

img= cv.imread('photos/1.jpg')
cv.imshow('luffy', img)

#translation ( shifting an image along the x and the y axes, up, down, left right ..)
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimentions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, -100, 100)
cv.imshow('translated', translated)

#rotation 
def rotate (img, angle, rotpoint=None):
    (height,width) = img.shape[:2]

    if rotpoint is None : 
        rotpoint = (width//2,height//2)
    
    rotMat= cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimentions= (width,height)
    return cv.warpAffine(img, rotMat, dimentions)
    
rotated = rotate(img, 45)
cv.imshow('rotated',rotated)

#rezizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resized',resized)

#flipping 
flip = cv.flip(img, 1)
cv.imshow('fliped',flip)

#cropping
cropped = img[200:400,300:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)