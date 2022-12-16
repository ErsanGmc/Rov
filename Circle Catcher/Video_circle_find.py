import cv2
import numpy as np

# Initialize the video capture
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the camera
    _, frame = cap.read()

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of colors to detect (in this case, red)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    

    # Create a mask to only select pixels that are red
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find the contours of the red objects in the frame
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a rectangle around the contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Show the frame with the rectangles
    cv2.imshow('Live Video with Rectangles', frame)

    # Check if the user pressed 'q' to quit
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
