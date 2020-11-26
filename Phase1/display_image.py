import cv2 #importing package

path = r'D:\Workspace\code_ground\OpenCV\1.image_webcam_video\1.1display_image\sunflower.jpg' #path where the image is saved

image = cv2.imread(path,1) #reading the image, 0 -> grayscale , 1 -> color image

cv2.imshow("Flower",image) #Displaying the image with the label "Flower"
cv2.waitKey(0) # 0 = infinite time | value = (second*1000)

cv2.destroyAllWindows() #Closes all windows
