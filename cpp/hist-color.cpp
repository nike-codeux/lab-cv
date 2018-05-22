#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;
 
int main()
{
	Mat origen;
	origen = imread("puppy.jpg", IMREAD_COLOR);
 
	if(!origen.data) {
		printf("Error al cargar imagen origen\n"); 
		return -1;
	}

	vector<Mat> planosBGR;
	split(origen, planosBGR);

	int binsMax = 256;
	
	float rango[] = {0, 256};
	const float* histRango= {rango};

	bool uniforme = true; bool acumular = false;

	Mat histB, histG, histR;

	calcHist(&planosBGR[0], 1, 0, Mat(), histB, 1, &binsMax, &histRango, uniforme, acumular);
	calcHist(&planosBGR[1], 1, 0, Mat(), histG, 1, &binsMax, &histRango, uniforme, acumular);
	calcHist(&planosBGR[2], 1, 0, Mat(), histR, 1, &binsMax, &histRango, uniforme, acumular);

	int histAncho = 512; int histAlto = 400;
	int binAncho = cvRound((double)histAncho/binsMax);

	Mat histImagen(histAlto, histAncho, CV_8UC3, Scalar( 0,0,0) );

	normalize(histB, histB, 0, histImagen.rows, NORM_MINMAX, -1, Mat() );
	normalize(histG, histG, 0, histImagen.rows, NORM_MINMAX, -1, Mat() );
	normalize(histR, histR, 0, histImagen.rows, NORM_MINMAX, -1, Mat() );

	for(int i = 1; i < binsMax; i++)
	{
		line(histImagen, Point( binAncho*(i-1), histAlto - cvRound(histB.at<float>(i-1)) ) ,
                       Point( binAncho*(i), histAlto - cvRound(histB.at<float>(i)) ),
                       Scalar( 255, 0, 0), 2, 8, 0  );
      line(histImagen, Point( binAncho*(i-1), histAlto - cvRound(histG.at<float>(i-1)) ) ,
                       Point( binAncho*(i), histAlto - cvRound(histR.at<float>(i)) ),
                       Scalar( 0, 255, 0), 2, 8, 0  );
      line(histImagen, Point( binAncho*(i-1), histAlto - cvRound(histR.at<float>(i-1)) ) ,
                       Point( binAncho*(i), histAlto - cvRound(histR.at<float>(i)) ),
                       Scalar( 0, 0, 255), 2, 8, 0  );
	}

  
	imshow("Imagen", origen);
	imshow("Histograma RGB", histImagen);
 
	waitKey(0);
	return 0;
}

