# coding=utf-8
# name=hu_yang_jie
from PIL import Image
import numpy as np


def handle_img(img_path1, img_path2):
    img1 = np.array(Image.open(img_path1).convert('L'))
    img2 = np.array(Image.open(img_path2).convert('L'))
    for y in range(10, 210):
        for x in range(39, 80):
            result = abs(int(img1[x][y]) - int(img2[x][y]))
            if result > 180:
                return y

if __name__ == '__main__':
    file1 = 'cut1.png'
    file2 = 'cut2.png'
    handle_img(file1, file2)
