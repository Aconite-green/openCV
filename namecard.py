import sys
import cv2

src = cv2.imread('namecard1.jpg')

if src is None:
    print('image load failed')
    sys.exit()

#x, y 0.5배
src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

#threshold
th ,src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY or cv2.THRESH_OTSU)

#외곽선 검출
countours,_ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#print(len(countours)) 

for pts in countours:
    if cv2.contourArea(pts) < 1000:
        continue
    cv2.polylines(src, pts, True, (0,0,255))

cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)

cv2.waitKey()
