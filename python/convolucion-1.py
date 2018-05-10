import numpy as np
import cv2

DDEPTH = -1

kernel = np.array(([0, -1, 0], [-1, 5, -1],[0, -1, 0]), dtype="int")
#kernel = np.array(([0, 1, 0], [1, -4, 1],[0, -1, 0]), dtype="int")
#kernel = np.array(([1, 1, 1], [1, 1, 1],[1, 1, 1]), dtype="int")/9
#kernel = np.array(([-1, -1, -1], [-1, 8, -1],[-1, -1, -1]), dtype="int")

img_fuente = cv2.imread('./pics/puppies.jpg')
img_fuente = cv2.resize(img_fuente, (0,0), fx=0.25, fy=0.25)
#img_fuente = cv2.cvtColor(img_fuente, cv2.COLOR_BGR2GRAY)
img_convol = cv2.filter2D(img_fuente, DDEPTH, kernel)

cv2.imshow('imagen convolucionada', img_convol)
cv2.waitKey(0)

