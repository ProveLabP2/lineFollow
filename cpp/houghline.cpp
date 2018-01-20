/* Compile with:
 * $ g++ hough.cpp `pkg-config --cflags --libs opencv`
 */

#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main() {
    const char *filename = "test1.jpg";
    Mat img = imread(filename, 0);      /* loads an image from file to matrix type */
    if (img.empty()) {                  /* file not opened */
        cout << "Could not open test1.jpg";
        return -1;
    }

    Mat dst, cdst;
    Canny(img, dst, 50, 200, 3);        /* canny edge detection */
    cvtColor(dst, cdst, CV_GRAY2BGR);   /* recolor to grayscale (binary in reality) */

    vector<Vec4i> lines;
    HoughLinesP(dst, lines, 1, CV_PI/180, 50, 50, 10 ); /* apply transform */
    for( size_t i = 0; i < lines.size(); i++ ) {        /* draw lines */
        Vec4i l = lines[i];
        line( cdst, Point(l[0], l[1]), Point(l[2], l[3]), Scalar(0,0,255), 3, CV_AA);
    }
    imshow("source", img);
    imshow("detected lines", cdst); /* display detected lines -- needs to be fixed */

    return 0;
}
