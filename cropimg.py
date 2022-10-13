import numpy as np
import cv2

image = cv2.imread('classe.jpg')
y=50
x=170
h=100
w=400
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop)
cv2.imwrite("img.jpg",crop)
cv2.waitKey(0)