import cv2 as cv
import numpy as np 

img = cv.imread('photos/1.jpg')
cv.imshow('luffy',img)

#split the image
b,g,r = cv.split(img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge it 
merged = cv.merge([b,g,r])
cv.imshow('merged',merged)

#create an blank image using numpy
blank = np.zeros(img.shape[:2], dtype='uint8')
#display channels 
blue = cv.merge([b,blank,blank])
cv.imshow('blue2',blue)
red= cv.merge([blank,blank,r])
cv.imshow('red2',red)
green = cv.merge([blank,g,blank])
cv.imshow('green2',green)


cv.waitKey(0)