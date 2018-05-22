#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;
 
int main()
{
	Mat origen;
	origen = imread("puppy.jpg", IMREAD_GRAYSCALE);
 
	if(!origen.data) {
		printf("Error al cargar imagen origen\n"); 
		return -1;
	}

	int binsMax = 256;
	
	float rango[] = {0, 256};
	const float* histRango= {rango};

	bool uniforme = true; bool acumular = false;

	Mat histGRAY;

	calcHist(&origen, 1, 0, Mat(), histGRAY, 1, &binsMax, &histRango, uniforme, acumular);

	int histAncho = 512; int histAlto = 400;
	int binAncho = cvRound((double)histAncho/binsMax);

	Mat histImagen(histAlto, histAncho, CV_8UC1, Scalar( 0,0,0) );

	normalize(histGRAY, histGRAY, 0, histImagen.rows, NORM_MINMAX, -1, Mat() );

	for(int i = 1; i < binsMax; i++)
	{
		line(histImagen, Point( binAncho*(i-1), histAlto - cvRound(histGRAY.at<float>(i-1)) ) ,
                       Point( binAncho*(i), histAlto - cvRound(histGRAY.at<float>(i)) ),
                       Scalar( 255, 0, 0), 1, 8, 0  );
	}

  
	imshow("Imagen", origen);
	imshow("Histograma Grises", histImagen);
 
	waitKey(0);
	return 0;
}

