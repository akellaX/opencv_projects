import numpy as np
import cv2
import math

white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)
img = np.zeros((1000,1000,3), np.uint8)
#
cv2.rectangle(img, (0, 0), (100, 100), white, -1)
cv2.rectangle(img, (0, 100), (100, 200), gray, -1)
cv2.rectangle(img, (0, 200), (100, 300), black, -1)
cv2.circle(img,(50,50), 50, black, -1)
cv2.circle(img,(50,150), 50, white, -1)
cv2.circle(img,(50,250), 50, gray, -1)


cv2.rectangle(img, (100, 0), (200, 100), white, -1)
cv2.rectangle(img, (100, 100), (200, 200), gray, -1)
cv2.rectangle(img, (100, 200), (200, 300), black, -1)
cv2.rectangle(img, (125, 25), (175, 75), black, -1)
cv2.rectangle(img, (125, 125), (175, 175), white, -1)
cv2.rectangle(img, (125, 225), (175, 275), gray, -1)


cv2.rectangle(img, (200, 0), (300, 100), white, -1)
cv2.rectangle(img, (200, 100), (300, 200), gray, -1)
cv2.rectangle(img, (200, 200), (300, 300), black, -1)
a1 = np.array([[[225,75],[250,25],[275,75]]], dtype=np.int32)
cv2.fillPoly(img,a1,black)
a1 = np.array([[[225,175],[250,125],[275,175]]], dtype=np.int32)
cv2.fillPoly(img,a1,white)
a1 = np.array([[[225,275],[250,225],[275,275]]], dtype=np.int32)
cv2.fillPoly(img,a1,gray)

cv2.rectangle(img, (0, 300), (100, 400), white, -1)
cv2.rectangle(img, (0, 400), (100, 500), gray, -1)
cv2.rectangle(img, (0, 500), (100, 600), black, -1)
cv2.circle(img,(50,350), 50, gray, -1)
cv2.circle(img,(50,450), 50, black, -1)
cv2.circle(img,(50,550), 50, white, -1)

cv2.rectangle(img, (100, 300), (200, 400), white, -1)
cv2.rectangle(img, (100, 400), (200, 500), gray, -1)
cv2.rectangle(img, (100, 500), (200, 600), black, -1)
cv2.rectangle(img, (125, 325), (175, 375), gray, -1)
cv2.rectangle(img, (125, 425), (175, 475), black, -1)
cv2.rectangle(img, (125, 525), (175, 575), white, -1)

cv2.rectangle(img, (200, 300), (300, 400), white, -1)
cv2.rectangle(img, (200, 400), (300, 500), gray, -1)
cv2.rectangle(img, (200, 500), (300, 600), black, -1)
a1 = np.array([[[225,375],[250,325],[275,375]]], dtype=np.int32)
cv2.fillPoly(img,a1,gray)
a1 = np.array([[[225,475],[250,425],[275,475]]], dtype=np.int32)
cv2.fillPoly(img,a1,black)
a1 = np.array([[[225,575],[250,525],[275,575]]], dtype=np.int32)
cv2.fillPoly(img,a1,white)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", img)
cv2.waitKey(100000)


kernel1 = np.array([[-1/9, 0,1/9],[-1/9,0,1/9],[-1/9,0,1/9]])
dst1 = cv2.filter2D(img, -1, kernel1)

kernel2 = np.array([[-1/9, -1/9,-1/9],[0,0,0],[1/9,1/9,1/9]])
dst2 = cv2.filter2D(img, -1, kernel2)

cv2.imshow("IMAGE2",dst1)
cv2.waitKey(100000)


theNewImage  = np.zeros((1000,1000,3), np.uint8)

for i in range(len(dst1)):
    for j in range(len(dst1[i])):
      theNewImage[i][j][0] = math.sqrt(dst1[i][j] ** 2 + dst2[i][j] ** 2)
      theNewImage[i][j][1] = dst1[i][j]
      theNewImage[i][j][2] = dst2[i][j]
cv2.imshow("Image3", theNewImage)
cv2.waitKey(100000)
