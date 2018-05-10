import cv2

fuente = cv2.imread('puppy.jpg')

reducido = cv2.resize(fuente, (0,0), fx=0.5, fy=0.5)

cv2.imshow('original', fuente)
cv2.imshow('reducido', reducido)

cv2.waitKey(0)
cv2.destroyAllWindows()
