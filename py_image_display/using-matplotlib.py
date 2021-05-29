import cv2
import matplotlib.pyplot as plt
img = cv2.imread("./opencv-logo-white.png")
plt.imshow(img, interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
