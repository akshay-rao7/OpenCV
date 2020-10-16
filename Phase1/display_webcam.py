import cv2 #importing opencv package

camera_no = 1 #camera number

cap = cv2.VideoCapture(camera_no) #display streaming of webcam

cap.set(3,640) #specify length
cap.set(4,280) #specify breadth
cap.set(10,100) #specify brightness

while True:
    display, img = cap.read()
    cv2.imshow("Webcam_capture",img)
    if cv2.waitKey(1) & 0xFF == ord ('s'):
        break

