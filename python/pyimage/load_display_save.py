from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args()) # return dictionary

print(type(args))
print(args.keys())
print(args.values())

image = cv2.imread(args['image'])
print('shape: {}'.format(image.shape))
print('width: {} pixels'.format(image.shape[1]))
print('height: {} pixels'.format(image.shape[0]))
print('chanels: {} pixels'.format(image.shape[2]))

(b, g, r) = image[0, 0]
print('Pixel at (0,0) - Red: {}, Green: {}, Blue: {}'.format(r, g, b))

image[0,0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print('Pixel at (0, 0) - Red: :{}, Green: {}, Blue: {}'.format(r, g, b))

corner = image[0:100, 0:100];
cv2.imshow('Corner', corner)

image[0:100, 0:100] =  (0, 255, 0)

#cv2.imshow('My image', image)
cv2.imshow('Image updated', image)
cv2.waitKey(0)


