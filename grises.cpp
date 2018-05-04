#include <opencv2/opencv.hpp>
using namespace cv;

int main( int argc, char** argv )
{
	Mat origen;

	// Leer imagen
 	origen = imread("puppy.jpg", IMREAD_COLOR );

	if(!origen.data )
	{
   	printf( "No existe la imagen\n " );
   	return -1;
	}

	Mat destino;
	cvtColor(origen, destino, COLOR_BGR2GRAY); // convertido a grises

	//namedWindow( origen, WINDOW_AUTOSIZE );
	imshow( "Original", origen );
	imshow( "Grises", destino );

	waitKey(0);

	return 0;
}
