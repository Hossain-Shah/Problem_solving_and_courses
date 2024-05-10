import numpy as np


image = input().split(" ")
lumination = 0


for brightness in range(len(image)):
    categories = [int(brightness) for brightness in image[brightness].split(",")]
    lumination+= np.sum(categories) / 3
    
if(lumination / len(image) > 90):
    print('day')
else:
    print('night')