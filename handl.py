# coding=utf-8
# name=hu_yang_jie
from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt

# for list_np in img:
#     print list_np
#     time.sleep(0.1)
# print len(img)
sum_num = 0
# 方法一，竖向每十像素与相邻像素求差
# for l in range(11):
#     for h in range(250):
#
#         for i in range(10):
#             sum_num = sum_num + abs(int(img[i + l*10][h])-int(img[i + l*10][h+1]))
#         if sum_num > 1000:
#             print h, sum_num
#         sum_num = 0
# 方法二，竖向全部求差
# for l in range(259):
#     for i in range(110):
#         sum_num = sum_num + abs(int(img[i][l]) - int(img[i+1][l]))
#     if sum_num > 1500:
#         print l, sum_num
#     sum_num = 0

# 方法三，十像素求直角的差


def sum_num(x, y, img):
    s = 0
    for i in range(10):
        s = s + abs(int(img[x+i][y])-int(img[x+i][y-1]))+abs(int(img[x][y+i])-int(img[x-1][y+i]))
    return s


# 扫描图像（起始点不能是（0,0）不然图像矩阵下标过界，结束点也要减去扫描宽度）
def scan_img(file_name):
    img = np.array(Image.open(file_name).convert('L'))
    for y in range(5, 250-15): # 像素减10为了不使扫描过界
        for x in range(5, 110-15):
            sn = sum_num(x, y, img)
            if sn > 2800:
                # print y
                return y
if __name__ == '__main__':

    file_name = input('输入文件名')
    result_num = scan_img(file_name)
    print result_num
