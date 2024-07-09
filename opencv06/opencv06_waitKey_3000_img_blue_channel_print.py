# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('mksh.png')
b = img[:,:,0] # 藍色channel
print(b)
cv2.imshow('opencv06', img)
cv2.waitKey(3000) # 等案空白建
# 等3秒鐘,都沒按鍵,就離開
cv2.destroyAllWindows()