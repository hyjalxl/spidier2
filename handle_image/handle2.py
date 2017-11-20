# name=hu_yang_jie
# -*- coding:utf-8 -*-
__author__ = 'lwp'

import cv2
import numpy as np
import matplotlib.pyplot as plt

path ='bili.png' # 图片路径
lwpImg = cv2.imread(path) # 加载图片
gray_lwpImg = cv2.cvtColor(lwpImg, cv2.COLOR_BGR2GRAY) # 转为灰度图

# 画目标区域，参数分别为图片、左上坐标、右下坐标、框的颜色、框线条的粗细
lwpImg = cv2.rectangle(lwpImg, (290, 0), (310, 327), (0, 255, 0), 2)
# 显示标记后的图片
cv2.imshow('local_pixel', lwpImg)

# 提取图片像素值到矩阵
pixel_data = np.array(gray_lwpImg)
# 提取目标区域
box_data = pixel_data[:, 290:310]
# 矩阵行求和
pixel_sum = np.sum(box_data, axis=1)

# 画图
x = range(576)
fig = plt.figure(figsize=(4, 2))
ax1 = fig.add_subplot(1, 1, 1)
ax1.bar(x, pixel_sum, width=1) # x为每个条形到x轴0点的距离，width为每个条的宽度
plt.xlabel('X')
plt.ylabel('Y')
plt.title('edge_filter')
plt.grid(True)
plt.show()

key = cv2.waitKey(0) & 0xFF
if key == ord('q'): # 按q关闭窗口
    cv2.destroyAllWindows()