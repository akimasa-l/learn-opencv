import cv2
img = cv2.imread("./opencv-logo-white.png")
cv2.namedWindow("img",cv2.WINDOW_NORMAL)#WINDOW_NORMALにするとウィンドウサイズが変わる
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
