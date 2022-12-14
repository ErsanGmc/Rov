import cv2
import numpy as np
import matplotlib as plt



def img_show(winname,img):
    img=cv2.resize(img,dsize=[500,300],interpolation=cv2.WINDOW_NORMAL)
    cv2.imshow(winname, img)


img=cv2.imread("1/underwater.jpg",1)

img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v =cv2.split(img_hsv)
h_new=h+40
s_new=s+40
v_new=v+40
# img_show("test1",h)
# img_show("test2",s)
# img_show("test3",v)
img_show("real",img)
img_new=cv2.merge((h_new,s,v))
# img_show("test4",img_new)
img_new=cv2.cvtColor(img_new,cv2.COLOR_HSV2RGB)
img_show("test4_1",img_new)

img_new1=cv2.merge((h,s_new,v))
# img_show("test5",img_new1)
img_new1=cv2.cvtColor(img_new1,cv2.COLOR_HSV2RGB)
img_show("test5_1",img_new1)

img_new2=cv2.merge((h,s,v_new))
# img_show("test6",img_new2)
img_new2=cv2.cvtColor(img_new2,cv2.COLOR_HSV2RGB)
img_show("test6_1",img_new2)

cv2.waitKey(0)
cv2.destroyAllWindows()