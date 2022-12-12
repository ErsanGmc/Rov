import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(512,511),(250,0,0),5)
cv2.line(img,(50,400),(400,50),(0,250,0),5)

cv2.rectangle(img,(50,50),(400,400),(0,0,255),5)
cv2.rectangle(img,(40,40),(200,220),(0,0,255),-1)

cv2.circle(img,(50,50),60,(120,100,80),-1)
cv2.circle(img,(200,200),30,(40,10,8),5)

cv2.ellipse(img,(255,255),(100,50),0,0,180,(255,0,0),5)
cv2.ellipse(img,(100,50),(300,50),0,0,180,(25,20,80),-1)

pts=np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)
pts2=pts.reshape(-1,1,2)
cv2.polylines(img,[pts],True,(255,100,50),3)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"OpenCV",(10,200),font,4,(0,100,200),2),cv2.LINE_AA

cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


def Rectangle_Draw(image,x,y):
    cv2.rectangle(image,x,y,(0,0,255),5)
    cv2.putText(image,"DIKdortgen",x,cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
    cv2.imshow("resim",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
Rectangle_Draw(img,(100,20),(200,80))