import cv2

img_fuente = cv2.imread('./pics/test-cs50.jpg')
reducido = cv2.resize(img_fuente, (0,0), fx=0.25, fy=0.25)

area = cv2.selectROI('cortando', reducido, False)

cortado = reducido[ int(area[1]) : int(area[1] + area[3]), int(area[0]) : int(area[0] + area[2]) ]

cv2.imshow('cortado', cortado)
cv2.waitKey(0)
