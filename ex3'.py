import numpy as np
from skimage import io
import matplotlib.pyplot as plt


image = io.imread('face3.png')
# plt.imshow(image)
# plt.show()

# print(image.shape[0])
# print(image.shape[1])
# print(image.shape[2])


def rgb(image):
    r = image[:,:, 0]
    g = image[:, :, 1]
    b = image[:, :, 2]

    rgb_max = np.maximum.reduce([r,g,b])
    rgb_min = np.minimum.reduce([r, g, b])
    rule1 = np.logical_and.reduce([r>95, g>40, b>20, rgb_max-rgb_min>15, abs(r-g)>15, r>g, r>b])
    rule2 = np.logical_and.reduce([r > 220, g > 210, b > 170, abs(r - g) <= 15, r > b, g > b])
    result = np.logical_or(rule1, rule2)
    plt.imshow(result)
    plt.show()


# hsv(image)
rgb(image)