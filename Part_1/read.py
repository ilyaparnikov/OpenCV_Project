import cv2 as cv

# Photos
img = cv.imread('Photos/nature_large.jpg')

cv.imshow('Nature', img)
cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows
