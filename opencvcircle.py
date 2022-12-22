import cv2
import numpy as np


camera=cv2.VideoCapture(0)


if not camera.isOpened():
    print("Kamera taninmadi/ acilmati")
    exit()

while True:
    ret,frame =camera.read()
    frame=cv2.resize(frame,(540,400),fx=0,fy=0,interpolation=cv2.INTER_CUBIC)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.medianBlur(frame,5)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)

    circles=cv2.HoughCircles(frame,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0,)
    circles=np.uint16(np.around(circles))

    for i in circles[0,:]:
    # Cemberin dis katmaını
        cv2.circle(frame,(i[0],i[1],i[2],(0,255,0),2))
    # Cemberin merkezi

        cv2.circle(frame,(i[0],i[1],2,(0,255,0),3))
    cv2.imshow("Sonuc",frame)
    if cv2.waitKey(1)& 0xFF ==ord('q'):
        print("Kamera sonlandirildi")
        break
camera.release()
cv2.destroyAllWindows()
