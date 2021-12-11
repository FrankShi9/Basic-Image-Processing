import matplotlib.pyplot as plt
import cv2


image = cv2.imread('./aliasing.png')

down = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)

plt.figure(figsize=(60, 48))

plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original')

plt.subplot(122)
plt.imshow(down, cmap='gray')
plt.title('Alias')

plt.show(block=True)
