import cv2 as cv 
import numpy as np

img = cv.imread('photos/1.jpg')
cv.imshow('luffy',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank',blank)

#blur the image before findin the contours
blur= cv.GaussianBlur(img,(5,5), cv.BORDER_DEFAULT)
# detect the edges
canny = cv.Canny(blur, 125,175)
cv.imshow('canny edges',canny)

# find the contours, takes the edges and a mode
# hierarchies are the representations of contours
# CHAIN_APPROX_NONE: returns all the contours 
# CHAIN_APPROX_SIMPLES: it's just compresses all the contourns into simple ones that makes sense
# by blurin the image, the number of contours dicrease
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))
print(len(hierarchies))

# using threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY )
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))
cv.imshow('thresh',thresh)

#draw the contours on the blank image
cv.drawContours(blank,contours,-1,(0,0,255), 1)
cv.imshow('contours drawn', blank)

cv.waitKey(0)