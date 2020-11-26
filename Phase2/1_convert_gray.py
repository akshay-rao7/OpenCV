import cv2

source_path = "D:\Workspace\code_space\Computer Vision_old\Computer Vision 1.2\sunflower.jpg"

img = cv2.imread(source_path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Color image",img)
cv2.imshow("Grayscale image",imgGray)
cv2.waitKey(0)
