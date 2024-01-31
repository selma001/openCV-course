import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread('photos/1.jpg')
cv.imshow('luffy',img)

#BGR to grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
cv.imshow('gray',gray)

#BGR to HSV 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#BGR to RGB 
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
plt.imshow(rgb)
plt.show()

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr',hsv_bgr)

cv.waitKey(0)