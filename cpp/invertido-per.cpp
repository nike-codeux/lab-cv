#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
 
int main()
{
	Mat origen, copia;
	origen = imread("puppy.jpg", IMREAD_COLOR);
	copia = origen.clone();
 
	if(!origen.data) {
		printf("Error al cargar imagen origen\n"); 
		return -1;
	}

	if(!copia.data) {
		printf("Error al cargar copia de la imagen\n");
		return -1;
	}
 
	std::cout << "Imagen origen" << std::endl;
	std::cout << "Filas: "<< origen.rows << std::endl;
	std::cout << "Columnas: " << origen.cols << std::endl;
 
	for (int i = 0 ; i < origen.cols ; i++) {
		for (int j = 0 ; j < origen.rows ; j++) {
			Vec3b color2 = copia.at<Vec3b>(Point(i, j));
			Vec3b color1 = origen.at<Vec3b>(Point((copia.cols - 1) - i, j));

			color2.val[0] = color1.val[0]; // B
			color2.val[1] = color1.val[1]; // G
			color2.val[2] = color1.val[2]; // R

    		copia.at<Vec3b>(Point(i,j)) = color1;
		}
	}
  
	imshow("Imagen Original", origen);
	imshow("Copia de la imagen", copia);
 
	waitKey(0);
	return 0;
}
