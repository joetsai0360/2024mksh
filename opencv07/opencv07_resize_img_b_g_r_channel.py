# -*- coding: utf-8 -*-
import cv2
img = cv2.imread('RGB.jpg')
img = cv2.resize( img, (400,400))

cv2.imshow('RGB', img)


b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

rrr = cv2.merge([r,r,r])
cv2.imshow('RRR',rrr)
ggg = cv2.merge([g,g,g])
cv2.imshow('GGG',ggg)
bbb = cv2.merge([b,b,b])
cv2.imshow('BBB',bbb)

cv2.waitKey(0)
cv2.destroyAllWindows()