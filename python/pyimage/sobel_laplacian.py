import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path of image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', image)

# CV_64F : 64bit float
# for transitions black-white (1) and white-black (2)
# (1) positive slope
# (2) negative slope
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian', lap)
cv2.waitKey(0)

# Sobel gradient magnitude x-axis
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
# Sobel gradient magnitude y-axis
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow('Sobel X', sobelX)
cv2.imshow('Sobel Y', sobelY)
cv2.imshow('Sobel combined', sobel)
cv2.waitKey(0)
