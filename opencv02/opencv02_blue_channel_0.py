# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('onepiece.jpg')
b = img[:,:,0]

cv2.imshow('opencv02', img)
cv2.imshow('blue', b)
cv2.waitKey(0) #K大寫