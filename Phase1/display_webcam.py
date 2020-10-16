import cv2 #importing package

camera_no = 1

cap = cv2.VideoCapture(camera_no)

cap.set(3,640)
cap.set(4,280)
cap.set(10,100)

while True:
    display, img = cap.read()
    cv2.imshow("Webcam_capture",img)
    if cv2.waitKey(1) & 0xFF == ord ('s'):
        break




