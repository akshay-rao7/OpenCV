import cv2

source_path = "D:\Workspace\code_space\Computer Vision\Computer Vision 1.1\img1.jpg"

img = cv2.imread(source_path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#(7,7) = always odd
#sigmaX = 0
cv2.imshow("Normal",img)
cv2.imshow("Gray image",imgGray)
cv2.imshow("Gaussian blur",imgBlur)
cv2.waitKey(0)