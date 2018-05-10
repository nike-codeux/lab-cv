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

	Mat destino;
	resize(origen, destino, Size(), 0.5, 0.5, INTER_AREA);

	imshow( "Original", origen);
	imshow( "Destino", destino);

	waitKey(0);

	return 0;
}
