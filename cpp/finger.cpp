#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

int main()
{
  cv::VideoCapture cap(0);
  const char* windowName = "Fingertip detection";
  int minH = 130, maxH = 160, minS = 10, maxS = 40, minV = 75, maxV = 130;
  cv::namedWindow(windowName);
  cv::createTrackbar("MinH", windowName, &minH, 180);
  cv::createTrackbar("MaxH", windowName, &maxH, 180);
  cv::createTrackbar("MinS", windowName, &minS, 255);
  cv::createTrackbar("MaxS", windowName, &maxS, 255);
  cv::createTrackbar("MinV", windowName, &minV, 255);
  cv::createTrackbar("MaxV", windowName, &maxV, 255);
  while (1)
  {
      cv::Mat frame;
      cap >> frame;
      cv::Mat hsv;
      cv::cvtColor(frame, hsv, CV_BGR2HSV);
      cv::inRange(hsv, cv::Scalar(minH, minS, minV), cv::Scalar(maxH, maxS, maxV), hsv);
      cv::imshow(windowName, hsv);
      if (cv::waitKey(30) >= 0) break;
  }
  return 0;
}
