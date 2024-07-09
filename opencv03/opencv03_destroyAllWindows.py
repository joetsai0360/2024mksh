# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('onepiece.jpg')
b = img[:,:,0] #0藍色
g = img[:,:,1] #1綠色
r = img[:,:,2] #2紅色

cv2.imshow('opencv02', img)
cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)
cv2.waitKey(0) #K大寫

cv2.waitKey(0) 
#如果按下任意鍵,全部視窗關閉
cv2.destroyAllWindows() 