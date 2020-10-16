import cv2 #importing opencv package

path = 'D:\Workspace\code_space\OpenCV_tutorial\img1.jpg' #mention the path from where the image will be read

image = cv2.imread(path) #reading the image

cv2.imshow("surprise",image)  #display the image window labelled "surprise"
cv2.waitKey(0) #continue displaying it 
