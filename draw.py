import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#1. paint the image a certain color
blank[200:300 , 300:400] = 0,0,255
cv.imshow('green', blank)

#2. draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow('rectangle', blank)

#3. draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40,(0,0,255), thickness=-1)
cv.imshow('circle',blank)

#4. draw line
cv.line(blank, (0,0),(blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('line',blank)

#5.write text in the image
cv.putText(blank,'hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)
cv.imshow('text', blank)
cv.waitKey(0)