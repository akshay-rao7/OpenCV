import cv2 #importing package

path = "D:\Workspace\code_space\OpenCV_tutorial\intro.mp4"

capture = cv2.VideoCapture(path)

while True:
    display , img = capture.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(30) & 0xFF == ord ('s'):
        break
