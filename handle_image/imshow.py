# coding=utf-8
# name=hu_yang_jie
import cv2
import numpy as np

img = cv2.imread('bili2.png')
cv2.imshow('lena', img)
cv2.waitKey(500)
blured = cv2.blur(img, (5, 5))
cv2.imshow('Blur', blured)
cv2.waitKey(500)
gray = cv2.cvtColor(blured, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.waitKey(500)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closed', closed)
cv2.waitKey(20000)
