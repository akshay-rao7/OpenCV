import cv2 #importing package

path = 'D:\code_base\lenna.jpg' #path where the image is saved

image = cv2.imread(path,1) #reading the image, 0 -> grayscale , 1 -> color image

cv2.imshow("Title",image) #Displaying the image with the label "Lenna"
cv2.waitKey(2000) # 0 = infinite time | value = (second*1000)

cv2.destroyAllWindows() #Closes all windows
