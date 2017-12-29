#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <stdlib.h>
#include <stdio.h>
#include <opencv2/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

Mat img, bimg, gbimg;
Mat dst;

int lowThres; // all edges lower than this value will be excluded
int highThres; //all edges above this value will be included

int main( int argc, char** argv ){
	
  cout << "Lower Threshold: ";	//let user input lower and upper threshold values
  cin >> lowThres;
  cout << endl;
  cout << "Upper Threshold: ";
  cin >> highThres;
  cout << endl;
	
  img = imread("lion.jpg", CV_LOAD_IMAGE_UNCHANGED); //define the image
	
  if( img.empty() ){
  cout << "Could not load or find the image" << endl;
  return -1;
  }	

  blur (img, bimg, Size (3,3) ); //blur the image
  cvtColor(bimg, gbimg, CV_BGR2GRAY ); //convert to greyscale
	
  Canny( gbimg, dst, lowThres, highThres); //run the canny edge function to convert the image to its edges

  namedWindow( "Edges", CV_WINDOW_AUTOSIZE );
  imshow( "Edges", dst ); //display the edges
  namedWindow("Original", CV_WINDOW_AUTOSIZE );
  imshow("Original", img ); //display the original
  waitKey(0);
  return 0;	
}
