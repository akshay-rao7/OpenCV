import cv2  #importing the libraries
import numpy as np #importing the libraries

img = np.zeros((512,512,3),np.uint8)



#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
#cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPENCV",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)



cv2.imshow("Image",img)

=======
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)



#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
#cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPENCV",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)



cv2.imshow("Image",img)

>>>>>>> 3417b42ddd8d7034ddae40543b67d63aa7de97d4
cv2.waitKey(0)
