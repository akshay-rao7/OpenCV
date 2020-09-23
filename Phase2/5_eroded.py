import cv2
import numpy as np

source_path = "D:\Workspace\code_space\Computer Vision\Computer Vision 1.1\img1.jpg"

img = cv2.imread(source_path)
kernel = np.ones((5,5),np.uint8)


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,200,100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Normal",img)
cv2.imshow("Gray image",imgGray)
cv2.imshow("Gaussian blur",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialated image",imgDialation)
cv2.imshow("Eroded image",imgEroded)


cv2.waitKey(0)