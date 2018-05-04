import cv2

fuente = 	cv2.imread('puppy.jpg')
copia = cv2.cvtColor(fuente, cv2.COLOR_BGR2GRAY)

#cv2.imwrite('./pics/gris-cs50.jpg', img_grises)

cv2.imshow('original', fuente)
cv2.imshow('grises', copia)

cv2.waitKey(0)
cv2.destroyAllWindows()
