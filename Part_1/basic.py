import cv2 as cv

img = cv.imread('Photos/nature.jpg')
cv.imshow('Nature', img)

# # Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# # Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=4)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=4)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[200:300, 300:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
