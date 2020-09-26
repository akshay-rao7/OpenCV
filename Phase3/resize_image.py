import cv2
print("package imported")

img = cv2.imread("img1.jpg")
print(img.shape) #displays the size of the image

imgResize = cv2.resize(img,(400,400))

cv2.imshow("Image",img)
cv2.imshow("Resized_mage",imgResize)
print(imgResize.shape)
cv2.waitKey(0)