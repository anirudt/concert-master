''' Detect human skin tone and draw a boundary around it.
Useful for gesture recognition and motion tracking.

Inspired by: http://stackoverflow.com/a/14756351/1463143

Date: 08 June 2013
'''

def nothing():
    pass

# Required moduls
import cv2
import numpy


windowName = 'Camera Output'
# Create a window to display the camera feed
cv2.namedWindow(windowName)
Cr_min, Cr_max, Cb_min, Cb_max = 133, 150, 77, 127
"""
cv2.createTrackbar('Cr min', windowName, Cr_min, 255, nothing)
cv2.createTrackbar('Cr max', windowName, Cr_max, 255, nothing)
cv2.createTrackbar('Cb min', windowName, Cb_min, 255, nothing)
cv2.createTrackbar('Cb max', windowName, Cb_max, 255, nothing)
"""

# Constants for finding range of skin color in YCrCb
min_YCrCb = numpy.array([0,Cr_min,Cb_min],numpy.uint8)
max_YCrCb = numpy.array([255,Cr_max,Cb_max],numpy.uint8)

# Get pointer to video frames from primary device
videoFrame = cv2.VideoCapture(0)

# Process the video frames
keyPressed = -1 # -1 indicates no key pressed

while(keyPressed < 0): # any key pressed has a value >= 0

    # Grab video frame, decode it and return next video frame
    readSucsess, sourceImage = videoFrame.read()

    # Convert image to YCrCb
    imageYCrCb = cv2.cvtColor(sourceImage,cv2.COLOR_BGR2YCR_CB)

    # Find region with skin tone in YCrCb image
    skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)

    """
    cv2.imshow(windowName, skinRegion)
    if (cv2.waitKey(30) >= 0):
        break
    """

    # Do contour detection on skin region
    contours, hierarchy = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contour on the source image
    max_area, max_area_idx = 0, 0
    for i, c in enumerate(contours):
        if (cv2.contourArea(c) > max_area):
            max_area = cv2.contourArea(c)
            max_area_idx = i
    cv2.drawContours(sourceImage, contours, max_area_idx, (0,255,0), 3)

    # Display the source image
    cv2.imshow('Camera Output',sourceImage)

    # Check for user input to close program
    keyPressed = cv2.waitKey(1) # wait 1 milisecond in each iteration of while loop


# Close window and camera after exiting the while loop
cv2.destroyWindow('Camera Output')
videoFrame.release()
