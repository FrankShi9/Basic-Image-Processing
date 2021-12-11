import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from skimage import color
from skimage.color import rgb2hsv

image = io.imread('face.png')
# plt.imshow(image)
# plt.show()

# print(image.shape[0])
# print(image.shape[1])
# print(image.shape[2])

def hsv(image):
    hsv = rgb2hsv(image)
    plt.imshow(hsv)
    plt.show()
    # print(hsv.shape)
    result = np.zeros(shape=(image.shape[0], image.shape[1]), dtype=int)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(hsv[i,j,0] > 50/180 and hsv[i,j,0] < 150/180):
                result[i,j] = 255
    plt.imshow(result)
    plt.show()

def rgb(image):
    r = image[:,:, 0]
    g = image[:, :, 1]
    b = image[:, :, 2]
    flag1, flag2, flag3, flag4, flag5 = 0,0,0,0,0
    rule1, rule2 = 0,0
    result = np.zeros(shape=(image.shape[0],image.shape[1]), dtype=int)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            if r[i,j] > 95 and g[i,j] > 40 and b[i,j] > 20:
                flag1 = True
            if max(r[i,j], g[i,j], b[i,j]) - min(r[i,j], g[i,j], b[i,j]) > 15:
                flag2 = True
            if abs(r[i,j] - g[i,j]) > 15 and r[i,j] > g[i,j] and r[i,j] > b[i,j]:
                flag3 = True

            if flag1 and flag2 and flag3:
                rule1 = True

            if r[i,j] > 220 and g[i,j] > 210 and b[i,j] > 170:
                flag4 = True
            if abs(r[i,j] - g[i,j]) <= 15 and b[i,j] < r[i,j] and b[i,j] < g[i,j]:
                flag5 = True

            if flag4 and flag5:
                rule2 = True

            if rule1 or rule2:
                result[i,j] = 255
                print('255')
            else:
                result[i, j] = 0
                print('0')

    plt.imshow(result)
    plt.show()


# hsv(image)
# rgb(image)