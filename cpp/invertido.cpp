#include <opencv2/opencv.hpp>
using namespace cv;

int main( int argc, char** argv )
{
	Mat origen;

	// Leer imagen
 	origen = imread("puppy.jpg", IMREAD_COLOR);

	if(!origen.data )
	{
   	printf( "No existe la imagen\n " );
   	return -1;
	}

	Mat vertical;
	Mat horizontal;
	Mat ambos;
	flip(origen, vertical, 0);
	flip(origen, horizontal, 1);
	flip(origen, ambos, -1);

	imshow( "Original", origen);
	imshow( "Vertical", vertical);
	imshow( "Horizontal", horizontal);
	imshow( "Ambos", ambos);

	waitKey(0);

	return 0;
}
