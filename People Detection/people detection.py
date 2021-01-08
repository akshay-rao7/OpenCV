import cv2
import numpy as np

classify_body = cv2.CascadeClassifier(r'D:\Workspace\code_space\walk_detect\haarcascade_fullbody.xml')

vid_capture = cv2.VideoCapture("test_walk.mp4")

while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    frame =cv2.resize(frame, None, fx=0.7, fy=0.7, interpolation = cv2.INTER_LINEAR)
    grayscale_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies_detected = classify_body.detectMultiScale(grayscale_img, 1.2, 4)
    for (x,y,w,h) in bodies_detected:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('Detect window' , frame)
        print("person detected")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid_capture.release()
cv2.destroyAllWindows()
