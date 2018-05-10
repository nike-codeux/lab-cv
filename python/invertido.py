import cv2

fuente = cv2.imread('puppy.jpg')

#reducido = cv2.resize(img_fuente, (0,0), fx=0.25, fy=0.25)

vertical = cv2.flip(fuente, 0)
horizontal = cv2.flip(fuente, 1)
ambos = cv2.flip(fuente, -1)

cv2.imshow('original', fuente)
cv2.imshow('horizontal', horizontal)
cv2.imshow('vertical', vertical)
cv2.imshow('ambos', ambos)

cv2.waitKey(0)
cv2.destroyAllWindows()
