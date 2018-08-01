/*
	tranforma las intensidades aplicando funciones:
	inversa, raiz cuadrada y cubica
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
	
	Mat imagen;
	Mat ImagenResultadoLUT;

	imagen = imread(nombre);
	if (!imagen.data) {
		cout << "Error al cargar la imagen: " << nombre << endl;
		exit(1);
	}

	cvtColor(imagen, imagen, COLOR_BGR2GRAY);

	Mat lut(1,256,CV_8U);
	
	//intercambiar las instrucciones de la funcion: inversa, raiz cuadra, raiz cubica
	for (int i = 0; i < 256; i++){
		//lut.at<uchar>(i) = 255 - i;
		lut.at<uchar>(i) = pow( (float)i*255, (float)(1/2.0) );
		//lut.at<uchar>(i) = pow( (float)i, (float)3.0) / (255*255);
	}
	LUT(imagen, lut, ImagenResultadoLUT);

	namedWindow("Original");
	imshow("Original", imagen);

	namedWindow("ImagenResultadoLUT");
	imshow("ImagenResultadoLUT", ImagenResultadoLUT);

	waitKey(0);
	return 0;
}

