import cv2 
import imutils

cap=cv2.VideoCapture(0)

while True:
    _,frame =cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(gray,(5,5),0)
    thresh=cv2.threshold(blurred,60,255,cv2.THRESH_BINARY_INV)[1]
    
    width=int(frame.shape[1])
    height=int(frame.shape[0])
    
    cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    
    M=cv2.moments(cnts[0])
    cX=int(M["m10"] / M["m00"])
    cY=int(M["m01"] / M["m00"]) 
    
    offx=int(cX-width/2)
    offy=int(height/2-cY)
    
    cv2.drawContours(frame,[cnts[0]],-1,(0,255,0),1)
    cv2.circle(frame,(cX,cY),5,(255,0,0),-1)
    cv2.circle(frame,(width//2,height//2),5,(255,0,255),-1)
    cv2.line(frame,(cX,cY),(width//2,height//2),(0,0,255),1)
    cv2.putText(frame,"Dikdorgen Merkezi",(cX-50,cY-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
    cv2.putText(frame,"Resmin Merkezi",(width//2-50,height//2+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)  
    cv2.putText(frame,f'offset X = {offx}',(width-400,50),cv2.FONT_HERSHEY_SIMPLEX,1,0,2)  
    cv2.putText(frame,f'offset Y = {offy}',(width-400,80),cv2.FONT_HERSHEY_SIMPLEX,1,0,2)
    cv2.imshow("image",frame)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()