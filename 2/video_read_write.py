import cv2
import numpy as np
# camera = cv2.VideoCapture(0)

# # camera=cv2.resize(camera,[300,400],fx=0,fy=0,interpolation=cv2.WINDOW_GUI_NORMAL)
# if not camera.isOpened():
#     print("Kamera tanımandı")
#     exit()

# while True:
#     ret,frame =camera.read()
#     # Ekran boyutlarını ayarlıyor
#     frame=cv2.resize(frame,(540,400),fx=0,fy=0,interpolation=cv2.INTER_CUBIC)
#     # Görüntüyü Gray tonaja çeviriyor
#     frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#     if not ret:
#      # Kameradan görüntü alınıp alınmadığını kontrol eder
#         print("Kameradan görütü alınamadı")
#         break
#     cv2.imshow("Camera",frame)
#     # Kameradan görüntü alınırsa
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         print("Kamera sonlandırıldı")
#         break
# camera.release()
# cv2.destroyAllWindows()

# cap=cv2.VideoCapture("240underwater.mp4")

# while cap.isOpened():

#     ret,frame = cap.read()
#     frame=cv2.resize(frame,(500,500),fx=0,fy=0,interpolation=cv2.INTER_CUBIC)

#     #  Görüntüyü ekrana gösterir
#     cv2.imshow("Videodan okuma",frame)

#     gray_cap=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#     # Thresholding ayırma
#     Thresh= cv2.adaptiveThreshold(gray_cap,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)

#     # Thresholdingli görüntüyü gösteriyor
#     cv2.imshow("Thresh",Thresh)

# video  okuyup dosyaya kaydetme
# cam = cv2.VideoCapture(0)
# fourrc = cv2.VideoWriter_fourcc('M','J','P','G')

# out = cv2.VideoWriter("Deneme.avi", fourrc, 30.0, (640, 480))
# while cam.isOpened():
#     ret, frame = cam.read()
#     if not ret:
#         print("görüntü alınamadı")
#         break
#     out.write(frame)
#     cv2.imshow("kamera", frame)
#     if cv2.waitKey(1) == ord("q"):
#         print("videodan ayrıldınız")
#         break

# cam.release()
# out.release()
# cv2.destroyAllWindows()


