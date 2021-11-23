import random

import cv2

img = cv2.imread('IMG.jpg',1)
img = cv2.resize(img,(700,800))
#img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
print(type(img))
#print(img)
#print(img.shape) # 3*3 matrix of pixels(height,width,channels)=(rows,columns,color space(BGR))

#Changing pixels in the image
#Looping through first 100 rows of the image along the width
for i in range(100):
    for j in range(img.shape[1]):   #0:rows,1:coloumns,2:colors
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

#Copy and paste parts of image
tag = img[400:600,600:800]
img[100:300,500:600] = tag

cv2.imshow('image',img)
cv2.waitKey(10000)  #Waiting for 10 secs
cv2.destroyAllWindows()
cv2.waitKey(1)              # Stack overflow soln to close the window
cv2.waitKey(1)
#cv2.waitKey(1)
#cv2.waitKey(1)


