import cv2

img_original = 	cv2.imread('./pics/test-cs50.jpg')
img_grises = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
img_grises = cv2.resize(img_grises, (0,0), fx=0.25, fy=0.25)

#cv2.imwrite('./pics/gris-cs50.jpg', img_grises)

cv2.imshow('original', img_original)
cv2.imshow('grises', img_grises)

cv2.waitKey(0)
