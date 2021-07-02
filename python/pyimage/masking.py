import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path of the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

print('Shape image:', image.shape[:2])
mask1 = np.zeros(image.shape[:2], dtype='uint8')
(cx, cy) = (image.shape[1]//2, image.shape[0]//2)
print('cx:', cx, 'cy:', cy)
cv2.rectangle(mask1, (cx-75, cy-75), (cx+75, cy+75), 255, -1)
cv2.imshow('Mask rect.', mask1)

masked1 = cv2.bitwise_and(image, image, mask=mask1)
cv2.imshow('Mask rect to image', masked1)

mask2 = np.zeros(image.shape[:2], dtype='uint8')
cv2.circle(mask2, (cx, cy), 100, 255, -1)
cv2.imshow('Mask circ.', mask2)

masked2 = cv2.bitwise_and(image, image, mask=mask2)
cv2.imshow('Mask circ to image', masked2)

cv2.waitKey(0)
