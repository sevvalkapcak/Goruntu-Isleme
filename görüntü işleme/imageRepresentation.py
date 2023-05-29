import skimage                
import skimage.draw            
from skimage.draw import disk 
import numpy as np 

img = iio.imread(uri="data/eight.tif")
img[1,2]= 1.0
img[3,0]= 1.0
fig, ax = plt.subplots()
plt.imshow(img)
print(img)


