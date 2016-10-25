import numpy as np
import time
import pdb
import math
import cv2
import musicgen
from optparse import OptionParser
import matplotlib.pyplot as plt
from cmath import pi
desc = " This is a gesture based music synthesis tool. It has 2 modes of operation: \
        1. Using a centroid of the hands approach, this could accommodate both single and double hands. This creates a music file, specifications \
        of which are written in the README file. \
        2. Using a gesture based model, which accommodates 4 actions to play 4 corresponding songs."

# List of nice colors for the music-mapper
colors = [(255, 255, 255), (219, 10, 91), (207, 0, 15), (210, 82, 127), (154, 18, 179), (31, 58, 147), (22, 160, 133), (247, 202, 24), (249, 105, 14), (149, 165, 166), (103, 65, 114), (255, 255, 255)]

parser = OptionParser()
parser.add_option("-n", "--num", dest="num", type="int", default=2)
parser.add_option("-d", "--deb", dest="debug", action="store_true", default=False)
parser.add_option("-f", "--fre", dest="free", action="store_true", default=False)
parser.add_option("-g", "--ges", dest="gest", action="store_true", default=False)

def tan2deg(tan):
    rad = math.atan(tan)
    if rad > 0:
        return 180.0*rad/pi
    else:
        return 180 + 180.0*rad/pi

def getMinMax(hist_h, hist_s, hist_v):
    """ helper: Returns the minP, maxP from the histogram. """
    minH, maxH = 0, 14
    thresh_s = hist_s.max() * 5.0/100
    space_s, _ = np.where(hist_s > thresh_s)
    minS = space_s[0]
    maxS = space_s[-1]; itx = space_s.size - 1;
    while maxS > minS+90:
        itx-=1
        maxS = space_s[itx]

    thresh_v = hist_v.max() * 5.0/100
    space_v, _ = np.where(hist_v > thresh_v)
    minV = space_v[0]
    maxV = space_v[-1]; itx = space_v.size - 1;
    if maxV < 200:
        maxV = 200

    return minH, maxH, minS, maxS, minV, maxV

def getAngle(start, end, far):
    tan_A = (far[1] - start[1])*1.0/(start[0] - far[0])
    tan_B = (far[1] - end[1])*1.0/(end[0] - far[0])
    a, b = tan2deg(tan_A), tan2deg(tan_B)
    print start, end, far
    print a, b
    angle = abs(a-b)
    return angle

def generateWallpaper(shape):
    namedWindow = "Wallpaper"
    white = np.ones(shape, dtype=np.uint8) * 255
    x,y,h,k = 0,0,53,48
    for i in xrange(12):
        for j in xrange(10):
            cv2.rectangle(white, (x+i*53, y+j*48), (h+i*53, k+j*48), tuple([0.1*j*comp for comp in colors[i]]), -1)
    #cv2.namedWindow(namedWindow, 0)
    #cv2.imshow(namedWindow, white)
    #cv2.imwrite("wallpaper.png", white)
    #cv2.waitKey(0)
    return white

def drawRectangles(img):
    rows = img.shape[0]
    cols = img.shape[1]
    i, j = cols/2, rows/2
    # Mark 8 rectangles.
    cv2.rectangle(img, (i-50,j-100), (i+50, j+100), (255, 255, 0), 1)

    # Return in the form of (rows, cols, 8).
    return img

def skin_detect_hsv(frame, opt, hsvt=None):
    erosion_size = 5
    dil_size = 4
    median_size = 4
    if opt is 'wo_ref':
        # Algorithm when a reference is absent

        minH, maxH, minS, maxS, minV, maxV = 0, 14, 66, 154, 110, 238


    if opt is 'wt_ref':
        # Algorithm when a reference is present

        hist_h = cv2.calcHist([hsvt], [0], None, [256], [0, 256])
        hist_s = cv2.calcHist([hsvt], [1], None, [256], [0, 256])
        hist_v = cv2.calcHist([hsvt], [2], None, [256], [0, 256])
        minH, maxH, minS, maxS, minV, maxV = getMinMax(hist_h, hist_s, hist_v)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.inRange(hsv, np.array([minH, minS, minV]), np.array([maxH, maxS, maxV]))

    erode_element, dil_element = None, None
    erode_element = cv2.getStructuringElement(cv2.MORPH_RECT, (2*erosion_size+1, 2*erosion_size+1), (erosion_size, erosion_size))
    dil_element = cv2.getStructuringElement(cv2.MORPH_RECT, (2*dil_size+1, 2*dil_size+1), (dil_size, dil_size))
    hsv = cv2.medianBlur(hsv, median_size*2+1)
    hsv = cv2.dilate(hsv, np.ones((9,9),np.uint8))
    bhsv = hsv

    cv2.imshow("binarized", hsv)
    cv2.waitKey(25)

    # Contour Detection
    contours = None

    cv2.waitKey(50)
    contours, hierarchy = cv2.findContours(hsv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return bhsv, contours, hierarchy

def skin_detect_ycbcr(frame):
    """Uses the YCbCr space to detect the skin regions. """
    Cr_min, Cr_max, Cb_min, Cb_max = 133, 150, 77, 127
    # Constants for finding range of skin color in YCrCb
    min_YCrCb = np.array([0,Cr_min,Cb_min], np.uint8)
    max_YCrCb = np.array([255,Cr_max,Cb_max], np.uint8)

    # Convert image to YCrCb
    imageYCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
    # Find region with skin tone in YCrCb image
    skinRegion = cv2.inRange(imageYCrCb, min_YCrCb, max_YCrCb) 
    # Do contour detection on skin region
    contours, hierarchy = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return imageYCrCb, contours, hierarchy

def gesture_single(img, contours, largestContour):
    """ Handles the largest Contour and returns the gesture ID. """
    cnt = contours[largestContour]
    hull = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull)
    junctions = []

    # For each defect, find the angles associated.
    for row in xrange(defects.shape[0]):
        # Handle the returns.
        start, end, far, dist = defects[row,0]
        start = tuple(cnt[start][0])
        end = tuple(cnt[end][0])
        far = tuple(cnt[far][0])
        print start, end, far
        theta = getAngle(start, end, far)
        # TODO: Impose some restrictions on theta and distance for detection.
        cv2.line(img,start,end,[0,255,0],2)
        cv2.circle(img,far,5,[0,0,255],-1)
        cv2.imshow("Concert", img)
        cv2.waitKey(25)
        print dist
        # Primary filter: Test if distance > 20k.
        if dist < 18000:
            continue
        else:
            print theta
            print "Junction detected!"
            pdb.set_trace()
            # Append the angle to the row for further fun
            junc = list(defects[row, 0])
            junc.append(theta)
            junctions.append(junc)

    junctions = np.array(junctions)
    return junctions


def webCamCapture():
    cap = cv2.VideoCapture(0)
    windowName = "Concert"
    erosion_size = 5
    dil_size = 4
    median_size = 4
    centroids = []
    print "Let us start now!"
    time.sleep(5)
    print "Projecting for next 10 seconds."
    start = time.time()
    itx = 0
    red_val = 0
    gest_count= np.zeros(4)
    (opts, args) = parser.parse_args()

    # TODO: Make a system here to capture hand color and decide the boundaries for H, S, V for thresholding.
    start = time.time()
    if opts.debug is True:
        roi_h = roi_s = roi_v = np.array([])
        while True:
            ret, frame = cap.read()
            frame = drawRectangles(frame)
            rows = frame.shape[0]
            cols = frame.shape[1]
            cv2.imshow("initing", frame)
            cv2.waitKey(25)
            if (time.time()-start > 8):
                # Slice the required search target
                target = frame[rows/2-50:rows/2+50, cols/2-100:cols/2+100]
                hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
                cv2.destroyWindow("initing")
                
                # Do a HSV histogram analysis here.
                #plt.hist(hsvt[:,:,0].ravel(), 256, [0, 256])
                #plt.show()
                #plt.hist(hsvt[:,:,1].ravel(), 256, [0, 256])
                #plt.show()
                #plt.hist(hsvt[:,:,2].ravel(), 256, [0, 256])
                #plt.show()

                break

            # TODO: Using the median, mean, decide the threshold. Probably have a trackbar to decide this too.

    while True:
        # Capture the frames one by one
        ret, frame = cap.read()
        X = max(frame.shape) 
        if itx == 0: 
            wallpaper = generateWallpaper(frame.shape)
            itx = 1

        hsv, contours, hierarchy = skin_detect_ycbcr(frame)

        # TODO: Logic here for both the hands
        # Generate their areas first.
        secLarge, largestContour = 0, 0
        for i in range(len(contours)):
            if (cv2.contourArea(contours[i]) > cv2.contourArea(contours[largestContour])):
                secLarge = largestContour
                largestContour = i

        cv2.drawContours(hsv, contours, largestContour, np.array([0, 0, 255]), 1);
        new_wp = wallpaper
        if len(contours) == 0:
            continue

        if opts.num == 1:
            print "One hand", red_val
            if opts.gest:
                junctions = gesture_single(hsv, contours, largestContour)
                pdb.set_trace()
                # TODO: On the basis of the number of junctions identified,
                # choose a certain music piece.
                gest_id = sum(junctions[:,4] < 80) % 4

                # TODO: Add this to the help-print text.
                
                # Draw the gesture selected, and in case this gesture is counted for 10 times, we go ahead with implementing it.
                if gest_count[gest_id] >= gest_thresh:
                    print "Selecting gesture id: {0}".format(gest_id)
                    musicgen.play_song(gest_id)
                    break

            elif opts.free:
                first = cv2.moments(contours[largestContour])
                first_cx = int(first['m10']/first['m00'])
                first_cy = int(first['m01']/first['m00'])
                centroids.append(first_cx)
                centroids.append(first_cy)
            

                cv2.circle(frame, (first_cx, first_cy), 5, (0, 0, red_val), -1)
                cv2.imshow(windowName, hsv)

        if opts.num == 2:
            print "Two hands"
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

            new_wp = wallpaper
            cv2.circle(new_wp, (X-first_cx, first_cy), 5, (0, 0, red_val), -1)
            cv2.circle(new_wp, (X-second_cx, second_cy), 5, (0, 0, red_val), -1)
            cv2.imshow(windowName, new_wp)
        else:
            print "Never here.", red_val, opts.num
        if time.time() > start + 25:
            break
        red_val += 0.5
        cv2.waitKey(25)

    cap.release()
    cv2.destroyAllWindows()
    cv2.imwrite("scatter.png", new_wp)

    if opts.fre:
        musicgen.proc(centroids, opts.num)
        print "Done with writing music files."

if __name__ == '__main__':
    time.sleep(3)
    webCamCapture()
