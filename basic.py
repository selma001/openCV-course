import cv2 as cv 

img = cv.imread('photos/1.jpg')
cv.imshow('luffy',img)

#converting to grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur an image ( removing noise using gaussian filter )
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur', blur) 

#Edge Cascade ( detect edges using canny, reduce the edges by applying a blur)
canny = cv.Canny(blur, 125,175)
cv.imshow('canny edges', canny)

#dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated',dilated)

#eroding
eroded = cv.erode(dilated,(7,7), iterations=3)
cv.imshow('eroded', eroded)

#resize
resized= cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)