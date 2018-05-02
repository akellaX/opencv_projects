import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread("man.jpg")
imagecv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.waitKey(0)

por = 100

image1 = imagecv[:,:,2]


msk = image1 > por
print(msk[125, 164])
msk1 = np.empty(msk.shape,dtype="uint8")
for i in range(msk.shape[0]):
    for j in range(msk.shape[1]):
        if msk[i, j] == True:
            msk1[i, j] = int(1)
        else:
            msk1[i,j]= int(0)


res = cv.bitwise_and(image, image, mask = msk1)

cv.imshow('image1', res)
cv.waitKey(0)
cv.destroyWindow('image1')