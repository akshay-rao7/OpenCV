import cv2

path = 'D:\Workspace\code_space\OpenCV_tutorial\img1.jpg'

image = cv2.imread(path) #reading the image

cv2.imshow("surprise",image)
cv2.waitKey(0)
