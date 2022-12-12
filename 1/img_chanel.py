import cv2
import matplotlib.pyplot as plt
import numpy as np
 


def img_show(winname,img):
    img=cv2.resize(img,dsize=[500,300],interpolation=cv2.WINDOW_NORMAL)
    cv2.imshow(winname, img)

def BGR2RGB(self, img):
        b, g, r = cv2.split(img)
        rgb_img = cv2.merge([r, g, b])
        return rgb_img
def RGB2BGR(self, img):
        r, g, b = cv2.split(img)
        bgr_img = cv2.merge([b, g, r])
        return bgr_img
img=cv2.imread("1/underwater.jpg",1)

img_show("Real",img)
# img_show("Second",ImgCov(img))

b,g,r=cv2.split(img)
img_show("Blue Channel",b)
img_show("Green Channel",g)
img_show("Red Channel",r)
img=cv2.cvtColor(img,BGR2RGB,)
img_show("Rea1l",img)
img_merged=cv2.merge((g,b,r))
img_show("Merged1",img_merged)

img_merged=cv2.merge((r,g,b))
img_show("Merge2",img_merged)

img_merged=cv2.merge((b,r,g))
img_show("Merged3",img_merged)



cv2.waitKey(0)
cv2.destroyAllWindows()