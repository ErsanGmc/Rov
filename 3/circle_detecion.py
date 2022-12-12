# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# # Read image.
# img = cv2.imread('3/basic.jpg', cv2.IMREAD_COLOR)

# # Conver t to grayscale.
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Blur using 3 * 3 kernel.
# gray_blurred = cv2.blur(gray, (3, 3))

# # Apply Hough transform on the blurred image.
# detected_circles = cv2.HoughCircles(gray_blurred,
# 				cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
# 			param2 = 30, minRadius = 1, maxRadius = 40)

# # Draw circles that are detected.
# if detected_circles is not None:

# 	# Convert the circle parameters a, b and r to integers.
# 	detected_circles = np.uint16(np.around(detected_circles))

# 	for pt in detected_circles[0, :]:
# 		a, b, r = pt[0], pt[1], pt[2]

# 		# Draw the circumference of the circle.
# 		cv2.circle(img, (a, b), r, (0, 255, 0), 2)

# 		# Draw a small circle (of radius 1) to show the center.
# 		cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
# 		cv2.imshow("Detected Circle", img)
    
# 		cv2.waitKey(0)


# def circleDetection(src):
#     img = cv.imread(src)
#     img = cv.resize(img, (500, 400))
#     output = img.copy()
#     gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     blur = cv.medianBlur(gray_img, 5)
#     circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT,
#                               1, 100, 10, param1=130, param2=55, minRadius=5, maxRadius=0)

#     detected_circles = np.uint16(np.around(circles))

#     for (x, y, r) in detected_circles[0, :]:
#         cv.circle(output, (x, y), r, (0, 255, 0), 3)
#         cv.circle(output, (x, y), 2, (255, 0, 0), 3)

#     cv.imshow("Original Image", img)
#     cv.imshow("Output", output)
#     cv.waitKey()
#     cv.destroyAllWindows()

# circleDetection("3\shapes.jpg")


import numpy as np
import cv2

cap=cv2.VideoCapture(0)
# ret=cap.set(3,640)
# ret=cap(4,480)
font=cv2.FONT_HERSHEY_SIMPLEX
kernel=np.ones((5,5),np.uint8)

if cap.isOpened() is True:
	while(True):
		ret,frame=cap.read()
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  
		lower_green=np.array([35,50,100])
		upper_green=np.array([77,255,255])
		
		
		mask=cv2.inRange(hsv,lower_green,upper_green)
		opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
		bila=cv2.bilateralFilter(mask,10,200,200)
		edges=cv2.Canny(opening,50,100)
		circles=cv2.HoughCircles(
			edges,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=10,maxRadius=500
		)
		if circles is not None:
			for circle in circles[0]:
				x=int(circle[0])
				y=int(circle[1])
				r=int(circle[2])
				cv2.circle(frame, (x, y), r, (0, 0, 255), 3)
				cv2.circle(frame, (x, y), 3, (255, 255, 0), -1)
				text = 'x:  '+str(x)+' y:  '+str(y)
				cv2.putText(frame, text, (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA, 0)
		else:
			cv2.putText(frame, 'x: None y: None', (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA, 0)  
		cv2.imshow("frame",frame)
		cv2.imshow("mask",mask)
		cv2.imshow("edges",edges)
		k=cv2.waitKey(5)& 0xFF
		if k == 27:
			break
	cap.release()
	cv2.destroyAllWindows()
else:
    print("cap is not opened!!!")
      