# -*- coding: utf-8 -*-
# 我們要在這把視訊打開
import cv2
cap = cv2.VideoCapture(0)

while True:
    rret, img = cap.read()
    # 1000 ms 1秒
    # 33 ms 對應 1/30 秒(每張30秒)
    cv2.imshow('opencv08', img)
    if cv2.waitKey(33)==27:
        break #27對應ESC鍵
        
cv2.destroyAllWindows()