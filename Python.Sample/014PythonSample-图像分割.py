from skimage.io import imread
from skimage import color
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
cimage = imread('photo.jpg')
fig, ax = plt.subplots(figsize=(20, 20))
ax.imshow(cimage)
ax.axis('off')

# RGB转为LAB
lab_img = color.rgb2lab(cimage)
x, y, z = lab_img.shape

# 显示颜色
to_plot = cimage.reshape(x * y, 3)
colors_map = to_plot.astype(np.float) / 256

# 创建数据
scatter_x = []
scatter_y = []
for xi in range(x):
    for yi in range(y):
        L_val = lab_img[xi, yi][0]
        A_val = lab_img[xi, yi][1]
        B_val = lab_img[xi, yi][2]
        scatter_x.append(A_val)
        scatter_y.append(B_val)

plt.figure(figsize=(20, 20))
plt.xlabel("a* from green to red")
plt.ylabel("b* from blue to yellow")
plt.scatter(scatter_x, scatter_y, c=colors_map)
# 显示
plt.show()