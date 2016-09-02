import numpy as np
import cv2

def webCamCapture():
    cap = cv2.VideoCapture(0)
    while True:
        # Capture the frames one by one
        ret, frame = cap.read()

        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('frame', frame_hsv)
        cv2.waitKey(25)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    webCamCapture()

