#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
using namespace std;
using namespace cv;

int main()
{
  VideoCapture cap(0);
  const char* windowName = "Fingertip detection";
  
  // Decided after tuning.
  int minH = 0, maxH = 14, minS = 66, maxS = 154, minV = 110, maxV = 238;

  int erosion_size = 21, dil_size = 10;
  int max_elem = 2;
  int median_size = 21;

  // Trackbar for erosion, dilation.
  namedWindow(windowName);
  createTrackbar( "Erosion Size", windowName,
                        &erosion_size, 21);
  createTrackbar( "Dilation Size", windowName,
                        &dil_size, 21);
  createTrackbar( "Median blue kernel size", windowName,
                        &median_size, 10);
  while (1)
  {
      Mat frame;

      // Capture the camera input
      cap >> frame;
      Mat hsv;
      cvtColor(frame, hsv, CV_BGR2HSV);
      inRange(hsv, Scalar(minH, minS, minV), Scalar(maxH, maxS, maxV), hsv);

      Mat erode_element, dil_element;
      erode_element = getStructuringElement(MORPH_RECT, Size(2*erosion_size+1, 2*erosion_size+1),
                  Point(erosion_size, erosion_size));
      dil_element = getStructuringElement(MORPH_RECT, Size(2*dil_size+1, 2*dil_size+1),
                  Point(dil_size, dil_size));
      medianBlur(hsv, hsv, median_size*2+1);
      dilate(hsv, hsv, dil_element);
      //erode(hsv, hsv, erode_element);
      imshow(windowName, hsv);
      if (waitKey(30) >= 0) break;
  }
  return 0;
}
