import cv2 as cv

#reading images
img = cv.imread('photos/1.jpg')
cv.imshow('luffy',img)

#reading videos
# to use my webcam ==> capture=cv.VideoCapture(0) 
#rexcale imagaes

def rescaleFrame(frame, scale=0.75) :
    width =int( frame.shape[1] * scale )
    height = int( frame.shape[1] * scale )
    dimensions=(width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image= rescaleFrame(img)
cv.imshow('image',resized_image)

cv.waitKey(0)