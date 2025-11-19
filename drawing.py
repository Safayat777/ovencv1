import os
import cv2
img = cv2.imread(os.path.join('.','whiteboard.png'))
print(img.shape)
cv2.line(img,(100,150),(150,200),(0,255,0),2)
cv2.rectangle(img,(100,50),(150,350),(0,0,255),10)
cv2.circle(img,(100,100),100,(255,0,0),10)
cv2.putText(img,'New World!',(150,150), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),3)
cv2.imshow('img',img)
cv2.waitKey(0)