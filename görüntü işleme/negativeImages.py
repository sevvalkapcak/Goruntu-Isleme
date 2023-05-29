import cv2
import matplotlib.pyplot as plt


img_bgr = cv2.imread('image.jpg',1)
img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()


height, width, _ = img.shape

for i in range(0, height - 1):
	for j in range(0, width - 1):
		
	
		pixel = img[i, j]
		
		pixel[0] = 255 - pixel[0]
	
		pixel[1] = 255 - pixel[1]
		
		pixel[2] = 255 - pixel[2]
		
		img[i, j] = pixel


plt.imshow(img)
plt.show()



