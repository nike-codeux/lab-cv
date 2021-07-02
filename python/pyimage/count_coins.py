from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path of image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow('Image', image)

edged = cv2.Canny(blurred, 20, 125)
cv2.imshow('Edges', edged)

(cnt, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('#Coins: {} in the image'.format(len(cnt)))

coins = image.copy()
cv2.drawContours(coins, cnt, -1, (0, 255, 0), 2)
cv2.imshow('Coins', coins)
cv2.waitKey(0)

for (i, c) in enumerate(cnt):
    (x, y, w, h) = cv2.boundingRect(c)
    print('Coin #{}'.format(i+1))
    coin = image[y:y+h, x:x+w]
    cv2.imshow('Coin', coin)

    print('coin type:', coin.dtype, 'shape:', coin.shape)
    mask = np.zeros(image.shape[:2], dtype='uint8')
    (center, radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(center[0]), int(center[1])), int(radius), 255, -1)
    mask = mask[y:y+h, x:x+w]
    print('mask type:', mask.dtype, 'shape:', mask.shape)
    cv2.imshow('Masked coin', cv2.bitwise_and(coin, coin, mask=mask))
    cv2.waitKey(0)

