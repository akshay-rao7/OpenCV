import cv2

path = r'D:\Workspace\code_ground\OpenCV\1.image_webcam_video\1.1display_image\flower.jpg'

image = cv2.imread(path,1) #reading the image, 0 -> grayscale , 1 -> color

cv2.imshow("Image",image)
cv2.waitKey(5000) # value = (second*1000)
#cv2.waitKey(0) # 0 = infinite
#cv2.destroyWindow("Image")
cv2.destroyAllWindows()

cv2.imwrite("c3.jpg",image)