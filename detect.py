__author__ = "Osama Kashif"

import os
import torch
import cv2

# Directory name for whereever the application/script is being run.
dir_name = os.path.dirname(os.path.abspath(__file__))

# YOLOv5 Model to use.
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

# The YOLOv5 model detects one image at a time so images from stream saved and deleted one by one.

# Remove image saving folders.
if os.path.exists(dir_name+"/runs/detect/exp/image0.jpg"):
    os.remove(dir_name+"/runs/detect/exp/image0.jpg")
if os.path.exists(dir_name+"/runs/detect/exp"):
    os.rmdir(dir_name+"/runs/detect/exp")
if os.path.exists(dir_name+"/runs/detect"):
    os.rmdir(dir_name+"/runs/detect")
if os.path.exists(dir_name+"/runs"):
    os.rmdir(dir_name+"/runs")

while True:

    # Read the frame.
    _, img = cap.read()

    # Convert to RGB for use in model.
    colour = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Inference/Detection using model.
    results = model(colour)
    results.save()
    img_to_show = cv2.imread(dir_name+"/runs/detect/exp/image0.jpg")
    
    # Display.
    cv2.imshow('img', img_to_show) # Can be removed if display unnecessary.

    # Remove image saving folders.
    if os.path.exists(dir_name+"/runs/detect/exp/image0.jpg"):
        os.remove(dir_name+"/runs/detect/exp/image0.jpg")
    if os.path.exists(dir_name+"/runs/detect/exp"):
        os.rmdir(dir_name+"/runs/detect/exp")
    if os.path.exists(dir_name+"/runs/detect"):
        os.rmdir(dir_name+"/runs/detect")
    if os.path.exists(dir_name+"/runs"):
        os.rmdir(dir_name+"/runs")
    
    # Stop if escape key is pressed.
    k = cv2.waitKey(30) & 0xff #Issue: Close button does not stop the program.
    if k==27:
        
        # Remove image saving folders.
        if os.path.exists(dir_name+"/runs/detect/exp/image0.jpg"):
            os.remove(dir_name+"/runs/detect/exp/image0.jpg")
        if os.path.exists(dir_name+"/runs/detect/exp"):
            os.rmdir(dir_name+"/runs/detect/exp")
        if os.path.exists(dir_name+"/runs/detect"):
            os.rmdir(dir_name+"/runs/detect")
        if os.path.exists(dir_name+"/runs"):
            os.rmdir(dir_name+"/runs")
        
        break

# Release the VideoCapture object.
cap.release()