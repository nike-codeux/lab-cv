import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path of the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

print('Shape image: ', image.shape[0], image.shape[1])
# width know
# compute ratio of new height
r = 150.0/image.shape[1]
print('Ratio to new height: ', r)
dim = (150, int(image.shape[0]*r))
print('Dimension to new height: ', dim)

# dim = width, height
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Res. (width)', resized)

# height know
# compute ratio of new width
r = 50.0/image.shape[0]
print('Ratio to new width', r)
dim = (int(image.shape[1]*r), 50)
print('Dimension to new width', dim)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Res. (Height)', resized)

print('Resize via function')
resized = imutils.resize(image, width=100)
cv2.imshow('Resized via function: ', resized)

cv2.waitKey(0)
