/*
   Espacios de color RGB y Lab, usando funciones: 
   split() - divide una matriz multi-canal a varias matrices de un solo canal.
   cvtColor() - convierte un espacio de color a otro.
   Donde:
   L - Ligthness (Intensity) - Luminosidad
   a - color component ranging from Green to Magenta
   b - color component ranging from Blue to Yellow
*/

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main()
{
   char nombre[] = "carrito.jpg";
   Mat imRGB, imLab; // imRGB - Matriz para RGB, imLab - Matriz para Lab

   imRGB = imread(nombre);
   if (!imRGB.data) {
      cout << "Error al cargar la imagen: " << nombre << endl;
      exit(1);
   }

   vector<Mat> planos_bgr;
   split(imRGB, planos_bgr);

   cvtColor(imRGB, imLab, CV_BGR2Lab);
   vector<Mat> planos_lab;
   split(imLab, planos_lab);

   namedWindow("Original");
   imshow("Original", imRGB);

   namedWindow("Lab");
   imshow("Lab", imLab);

   namedWindow("L");
   imshow("L", planos_lab[0]);

   namedWindow("a");
   imshow("a", planos_lab[1]);

   namedWindow("b");
   imshow("b", planos_lab[2]);

   cvWaitKey(0);
   return 0;
}
