import cv2
import numpy as np

camera = cv2.VideoCapture(0)
def nothing(x):
    pass
cv2.namedWindow("frame")
cv2.createTrackbar("H1","frame",0,180,nothing)
cv2.createTrackbar("H2","frame",0,180,nothing)
cv2.createTrackbar("S1","frame",0,255,nothing)
cv2.createTrackbar("S2","frame",0,255,nothing)
cv2.createTrackbar("V1","frame",0,255,nothing)
cv2.createTrackbar("V2","frame",0,255,nothing)

while camera.isOpened():
    ret,frame =camera.read()
    
    
    cv2.imshow("Real",frame)
    # Ekran boyutlarını ayarlıyor    
    HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    H1=cv2.getTrackbarPos("H1","frame")
    H2=cv2.getTrackbarPos("H2","frame")
    S1=cv2.getTrackbarPos("S1","frame")
    S2=cv2.getTrackbarPos("S2","frame")
    V1=cv2.getTrackbarPos("V1","frame")   
    V2=cv2.getTrackbarPos("V2","frame")

    lower=np.array([H1,S1,V1])
    upper=np.array([H2,S2,V2])
    
    mask=cv2.inRange(HSV,lower,upper)
    cv2.imshow("HSV_Görüntü",HSV)
    masked_image=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("Kirmizi_Filtreli",masked_image)
    

    # Kameradan görüntü alınırsa
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Kamera sonlandirildi")
        break
camera.release()
cv2.destroyAllWindows()
