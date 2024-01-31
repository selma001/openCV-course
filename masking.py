import cv2 as cv
import numpy as np

img = cv.imread('photos/1.jpg')
cv.imshow('luffy',img)
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank',blank)

#using bitwise we can mask the images
mask = cv.circle(blank, (img.shape[1]//2 +100,img.shape[0]//2 + 80),100,255,-1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)

cv.waitKey(0)