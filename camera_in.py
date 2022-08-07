import sys
import cv2

cap = cv2.VideoCapture('vtest.avi')

if not cap.isOpend():
    print('camera open fail')
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break
    #edge detaction
    edge = cv2.Canny(frame, 50, 150)
    cv2.imshow('edge', edge)
    if cv2.waitKey(20) == 27:
        break

cap.release()
cap.destroyAllWindows()