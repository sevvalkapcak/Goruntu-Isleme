import cv2
import numpy as np

image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

sobel_x = cv2.Sobel(img_gaussian, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(img_gaussian, cv2.CV_64F, 1, 0, ksize=5)

img_sobel = sobel_x + sobel_y
cv2.imshow('Sobel ', img_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()