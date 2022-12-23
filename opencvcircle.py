import cv2
import numpy as np


# camera=cv2.VideoCapture("test2.mp4")
camera=cv2.VideoCapture(0)


while True:
    ret,frame =camera.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,50,50])
    upper_red=np.array([10,255,255])
    mask=cv2.inRange(hsv,lower_red,upper_red)
    frame=cv2.bitwise_and(frame,frame,mask=mask)

    frame=cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.medianBlur(frame,5)
    
    

    circles=cv2.HoughCircles(frame,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)

    circles=np.uint16(np.around(circles))
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)

    for i in circles[0,:]:
    # Cemberin dis katmaını
        cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
    # Cemberin merkezi

        cv2.circle(frame,(i[0],i[1]),2,(0,255,0),3)
    # out.write(frame)
    cv2.imshow("Sonuc",frame)
    if cv2.waitKey(1)& 0xFF ==ord('q'):
        print("Kamera sonlandirildi")
        break
camera.release()

cv2.destroyAllWindows()
