import cv2
import numpy as np

camera = cv2.VideoCapture(0)
def nothing(x):
    pass
cv2.namedWindow("Deneme13")
cv2.createTrackbar("H1","frame",0,359,nothing)
cv2.createTrackbar("H2","frame",0,359,nothing)
cv2.createTrackbar("S1","frame",0,255,nothing)
cv2.createTrackbar("S2","frame",0,255,nothing)
cv2.createTrackbar("V1","frame",0,252,nothing)
cv2.createTrackbar("V2","frame",0,252,nothing)

while camera.isOpened():
    ret,frame =camera.read()
    cv2.imshow("Real",frame)
    # Ekran boyutlarını ayarlıyor
    frame=cv2.resize(frame,(540,400),fx=0,fy=0,interpolation=cv2.INTER_CUBIC)
    
    HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    H1=cv2.getTrackbarPos("H1","FRAME")
    H2=cv2.getTrackbarPos("H2","FRAME")
    S1=cv2.getTrackbarPos("S1","FRAME")
    S2=cv2.getTrackbarPos("S2","FRAME")
    H3=cv2.getTrackbarPos("V1","FRAME")   
    H3=cv2.getTrackbarPos("VE","FRAME")

    lower=np.array([H1,S1,H1])
    upper=np.array([H2,S2,H3])
    
    mask=cv2.inRange(HSV,lower,upper)
    cv2.imshow("Video_without_Mask",HSV)
    masked_image=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("Video_with_Mask",masked_image)
    
    if not ret:
     # Kameradan görüntü alınıp alınmadığını kontrol eder
        print("Kameradan görütü alinamadi")
        break
    # Kameradan görüntü alınırsa
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Kamera sonlandirildi")
        break
camera.release()
cv2.destroyAllWindows()
