import cv2
import sys

#array 형태로 불러옴
img = cv2.imread('cat.bmp')

#about error
if img is None:
    print('Image load fail')
    sys.exit()

print(type(img))
print(img.shape)
print(img.dtype)

#on new window(name = image) show image
cv2.namedWindow('image')
cv2.imshow('image', img)
#waiting for keyinput
cv2.waitKey()
#cv2.destoryAllWindows()
