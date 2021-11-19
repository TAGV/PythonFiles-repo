import cv2

img = cv2.imread('IMG.jpg',-1)
img = cv2.resize(img,(400,400))
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('image',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
cv2.waitKey(1)              # Stack overflow soln to close the window
#cv2.waitKey(1)
#cv2.waitKey(1)
#cv2.waitKey(1)


