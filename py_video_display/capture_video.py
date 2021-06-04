import time
import cv2
cap= cv2.VideoCapture(0)
print(cap.isOpened())
for i in range(1):
    #time.sleep(0.5)
    ret,frame=cap.read()
    print(ret,frame)
    print(cap.isOpened())
    time.sleep(0.5)
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    time.sleep(0.5)
    print(cap.get(3),cap.get(4))
    #cv2.imwrite(f"frame{i}.jpg",gray)
    cv2.imshow(f"frame{i}.jpg",gray)
cap.release()

cv2.waitKey(0)

#time.sleep(60)
cv2.destroyAllWindows()
