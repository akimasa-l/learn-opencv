import cv2
img = cv2.imread("./opencv-logo-white.png")
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
