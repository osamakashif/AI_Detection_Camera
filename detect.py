__author__ = "Osama Kashif"

import cv2

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

while True:

    # Read the frame
    _, img = cap.read()
    
    # Display
    cv2.imshow('img', img) # Can be removed if display unnecessary
    
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff #Issue: Close button does not stop the program.
    if k==27:
        break

# Release the VideoCapture object
cap.release()