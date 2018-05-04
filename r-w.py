import cv2
 
imagen = cv2.imread("puppy.jpg")

''' Leer ''' 
dest_imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

cv2.imshow("Modificado", dest_imagen)
cv2.imshow("Original", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

''' Escribir ''' 
cv2.imwrite("puppy-copia.jpg", dest_imagen)
