import cv2 #importing opencv package

path = "D:\Workspace\code_space\OpenCV_tutorial\intro.mp4"  #mention the path from where the video(mp4 file) will be read

capture = cv2.VideoCapture(path) #reading the video

while True: #loop
    display , img = capture.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(30) & 0xFF == ord ('s'): #if "s" key pressed close video window
        break
