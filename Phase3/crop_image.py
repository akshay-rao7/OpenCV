import cv2
print("package imported")

img = cv2.imread("img1.jpg")
print(img.shape) #displays the size of the image

imgCropped = img[0:100,0:50]

cv2.imshow("Image",img)
cv2.imshow("Cropped_mage",imgCropped)

cv2.waitKey(0)