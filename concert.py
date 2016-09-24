import numpy as np
import pdb
import cv2

def webCamCapture():
    cap = cv2.VideoCapture(0)
    windowName = "Concert"
    minH, maxH, minS, maxS, minV, maxV = 0, 14, 66, 154, 110, 238
    erosion_size = 5
    dil_size = 4
    median_size = 4
    while True:
        # Capture the frames one by one
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv = cv2.inRange(hsv, np.array([minH, minS, minV]), np.array([maxH, maxS, maxV]))

        erode_element, dil_element = None, None
        erode_element = cv2.getStructuringElement(cv2.MORPH_RECT, (2*erosion_size+1, 2*erosion_size+1), (erosion_size, erosion_size))
        dil_element = cv2.getStructuringElement(cv2.MORPH_RECT, (2*dil_size+1, 2*dil_size+1), (dil_size, dil_size))
        hsv = cv2.medianBlur(hsv, median_size*2+1)
        hsv = cv2.dilate(hsv, np.ones((9,9),np.uint8))
        cv2.waitKey(25)

        # Contour Detection
        contours = None

        cv2.waitKey(50)
        contours, hierarchy = cv2.findContours(hsv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        largestContour = 0

        # TODO: Logic here for both the hands
        for i in range(len(contours)):
            if (cv2.contourArea(contours[i]) > cv2.contourArea(contours[largestContour])):
                largestContour = i
        print largestContour, len(contours)
        M = cv2.moments(contours[largestContour])
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        print cx, cy
        cv2.drawContours(frame, contours, largestContour, (0, 0, 255), 1);
        cv2.imshow(windowName, frame);
        cv2.waitKey(25)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    webCamCapture()

