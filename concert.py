import numpy as np
import time
import pdb
import cv2
import musicgen

colors = [(255, 255, 255), (219, 10, 91), (207, 0, 15), (210, 82, 127), (154, 18, 179), (31, 58, 147), (22, 160, 133), (247, 202, 24), (249, 105, 14), (149, 165, 166), (103, 65, 114), (255, 255, 255)]

def generateWallpaper(shape):
    namedWindow = "Wallpaper"
    white = np.ones(shape, dtype=np.uint8) * 255
    x,y,h,k = 0,0,53,48
    for i in xrange(12):
        for j in xrange(10):
            cv2.rectangle(white, (x+i*53, y+j*48), (h+i*53, k+j*48), tuple([0.1*j*comp for comp in colors[i]]), -1)
    cv2.namedWindow(namedWindow, 0)
    cv2.imshow(namedWindow, white)
    cv2.imwrite("wallpaper.png", white)
    cv2.waitKey(0)

def webCamCapture():
    cap = cv2.VideoCapture(0)
    windowName = "Concert"
    minH, maxH, minS, maxS, minV, maxV = 0, 14, 66, 154, 110, 238
    erosion_size = 5
    dil_size = 4
    median_size = 4
    centroids = []
    print "Let us start now!"
    time.sleep(5)
    print "Projecting for next 10 seconds."
    start = time.time()
    itx = 0
    while True:
        # Capture the frames one by one
        ret, frame = cap.read()
        if itx == 0: 
            wallpaper = generateWallpaper(frame.shape)
            itx = 1

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

        # TODO: Logic here for both the hands
        # Generate their areas first.
        secLarge, largestContour = 0, 0
        for i in range(len(contours)):
            if (cv2.contourArea(contours[i]) > cv2.contourArea(contours[largestContour])):
                secLarge = largestContour
                largestContour = i

        first = cv2.moments(contours[largestContour])
        second = cv2.moments(contours[secLarge])

        first_cx = int(first['m10']/first['m00'])
        first_cy = int(first['m01']/first['m00'])
        second_cx = int(second['m10']/second['m00'])
        second_cy = int(second['m01']/second['m00'])

        print first_cx, first_cy
        print second_cx, second_cy
        centroids.append(first_cx)
        centroids.append(first_cy)
        centroids.append(second_cx)
        centroids.append(second_cy)

        cv2.drawContours(frame, contours, largestContour, (0, 0, 255), 1);
        cv2.drawContours(frame, contours, secLarge, (0, 255, 0), 1);
        cv2.imshow(windowName, frame);
        if time.time() > start + 10:
            break
        cv2.waitKey(25)

    cap.release()
    cv2.destroyAllWindows()

    musicgen.proc(centroids)
    print "Done with writing music files."

if __name__ == '__main__':
    webCamCapture()

