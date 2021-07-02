import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path of the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

# crop (60, 340) rows,
# crop (150, 320) cols,
# start (60, 150) r0,c0 - ref: (x,y)
# end (340, 320) rn, cn - ref:  (x,y)
# start (150, 60) x0-cols0, y0-rows0 - ref: (y,x)
# end (320, 340) xn-colsn, yn-rowsn - ref: (y,x)
# numpy: 1th: Height, 2th: Width
cropped = image[60:340, 150:320]
cv2.imshow('Cropped', cropped)
print('Cropped dimensions: ', cropped.shape)
cv2.waitKey(0)
