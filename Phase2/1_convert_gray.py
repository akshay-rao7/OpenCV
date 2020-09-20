import cv2

source_path = "D:\Workspace\code_space\Computer Vision\Computer Vision 1.1\img1.jpg"

img = cv2.imread(source_path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Normal",img)
cv2.imshow("Gray",imgGray)
cv2.waitKey(0)