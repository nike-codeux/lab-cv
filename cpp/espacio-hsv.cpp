/*
   Espacios de color RGB y HSV, usando funciones: 
   split() - divide una matriz multi-canal a varias matrices de un solo canal.
   cvtColor() - convierte un espacio de color a otro.
   Donde:
   H - Hue (Dominant Wavelength) - Matiz
   S - Saturation
   V - Value (Intensity) - Brillo
*/

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main()
{
   char nombre[] = "puppy-2.jpg";
   Mat imRGB, imHSV; // imRGB - Matriz para RGB, imHSV - Matriz para HSV

   imRGB = imread(nombre);
   if (!imRGB.data) {
      cout << "Error al cargar la imagen: " << nombre << endl;
      exit(1);
   }

   vector<Mat> planos_bgr;
   split(imRGB, planos_bgr);

   cvtColor(imRGB, imHSV, CV_BGR2HSV);
   vector<Mat> planos_hsv;
   split(imHSV, planos_hsv);

   namedWindow("Original");
   imshow("Original", imRGB);

   namedWindow("HSV");
   imshow("HSV", imHSV);

   namedWindow("H");
   imshow("H", planos_hsv[0]);

   namedWindow("S");
   imshow("S", planos_hsv[1]);

   namedWindow("V");
   imshow("V", planos_hsv[2]);

   cvWaitKey(0);
   return 0;
}
