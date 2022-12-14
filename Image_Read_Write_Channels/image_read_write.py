import cv2
import numpy as np
from matplotlib import pyplot as plt

def img_show(img):
    cv2.imshow("win", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image=cv2.imread("1/underwater.jpg",0)
cv2.resize(image,dsize=[300,400],interpolation=cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.imshow("img",image)

plt.imshow(image,cmap="gray")
plt.show()

k=cv2.waitKey(0) 
if k ==ord("q"):
    print("q tuşuna basıldı")
    cv2.imwrite("grayimg",image)
cv2.destroyAllWindows()

