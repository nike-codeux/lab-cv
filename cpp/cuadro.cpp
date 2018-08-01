/*
	grafica un cuadro negro en la imagen desde
	1/4 a 3/4 tanto en filas como en columnas
*/

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main(int argc, char** argv)
{
   char nombre[] = "puppy-2.jpg";
   Mat imagen;
	
	imagen = imread(nombre);
	
	if(!imagen.data){
		cout << "Error al cargar la imagen: " << nombre << endl;
		exit(1);
	}

	for(int i = imagen.rows/4; i < 3*imagen.rows/4; ++i){
		for(int j = imagen.cols/4; j < 3*imagen.cols/4; ++j)
			imagen.at<Vec3b>(Point(i, j)) = Vec3b(0, 0, 0);
	}

	namedWindow("Original");
	imshow("Original", imagen);

	imwrite("cuadro-black.jpg", imagen);

	waitKey(0);

	return 0;
}
