import cv2 as cv

img = cv.imread('photos/1.jpg')
cv.imshow('luffy',img)

#Averaging ( define a kernal window )
average = cv.blur(img, (7,7))
cv.imshow('average blur',average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (7,7),0)
cv.imshow('guassian blur',gauss)

#median blur
median = cv.medianBlur(img,7)
cv.imshow('median',median)

#bilateral (src,diametre,colornumber,sigmaspace) best of all the bluring filters
bil = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral',bil)

cv.waitKey(0)