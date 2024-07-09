# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('onepiece.jpg')
b = img[:,:,0] #0藍色
g = img[:,:,1] #1綠色
r = img[:,:,2] #2紅色

img_rbb = cv2.merge([r,b,b])
cv2.imwrite('rbb.jpg', img_rbb)
cv2.imshow('RBB', img_rbb)
cv2.imshow('opencv04', img)

cv2.waitKey(0) 
#如果按下任意鍵,全部視窗關閉
cv2.destroyAllWindows() 