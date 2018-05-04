#include <opencv2/opencv.hpp>
using namespace cv;

int main( int argc, char** argv )
{
	char* origen = argv[1];
	Mat imagen;

	// Leer imagen
 	imagen = imread( origen, IMREAD_COLOR );

	if( argc != 2 || !imagen.data )
	{
   	printf( " No existe la imagen\n " );
   	return -1;
	}

	Mat dest_image;
	cvtColor( imagen, dest_image, COLOR_BGR2RGBA );

	namedWindow( origen, WINDOW_AUTOSIZE );
	imshow( origen, imagen );
	imshow( "Copia de imagen", dest_image );

	// Escribir imagen
	imwrite( "puppy-copia.jpg", dest_image );

	waitKey(0);

	return 0;
}
