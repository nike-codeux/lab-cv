from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

def plot_hist(image, title, mask=None):
    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    plt.figure()
    plt.title(title)
    plt.xlabel('Bins')
    plt.ylabel('#Bins')
    
    for (ch, color) in zip(chans, colors):
        hist = cv2.calcHist([ch], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path of image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)
plot_hist(image, 'Histograma original')

mask = np.zeros(image.shape[:2], dtype='uint8')
cv2.rectangle(mask, (150, 90), (200, 140), 255, -1)
cv2.imshow('Mask', mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Applying mask', masked)

plot_hist(image, 'Histogram masked', mask=mask)
plt.show()

cv2.waitKey(0)
