import cv2
import numpy as np
###the python code that configures the red circle in the image from the camera with opencv2 and draws a blue rectangle around it
# Read the image from the camera
image = cv2.imread('3/basic.jpg')

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range of colors to detect (in this case, red)
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

# Create a mask to only select pixels that are red
mask = cv2.inRange(hsv, lower_red, upper_red)

# Find the contours of the red objects in the image
_, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw a rectangle around the contours
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Show the image with the rectangles
cv2.imshow('Image with rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
