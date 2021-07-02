import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

# 1: flip horizontally around y-axis
flipped = cv2.flip(image, 1)
cv2.imshow('Flipped Horizontally', flipped)

# 0: flip vertically around x-axis
flipped = cv2.flip(image, 0)
cv2.imshow('Flipped Vertically', flipped)

# -1: flip around both axes
flipped = cv2.flip(image, -1)
cv2.imshow('Flipped H&V', flipped)

cv2.waitKey(0)
