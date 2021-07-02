from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path of the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)
cv2.waitKey(0)

# Histogram RGB 
plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins')
plt.ylabel('#Pixels')

chans = cv2.split(image)
colors = ('b', 'g', 'r')

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.show()

# Histograms multi-dimensional : 2D
fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
hist = np.array(hist)
p = ax.imshow(hist, interpolation='nearest')
ax.set_title('2D histogram G and B')
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation='nearest')
ax.set_title('2D histogram G and R')
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation='nearest')
ax.set_title('2D histogram B and R')
plt.colorbar(p)

plt.show()

print('2D histogram shape: {}, width {} values'.format(hist.shape, hist.flatten().shape[0]))

