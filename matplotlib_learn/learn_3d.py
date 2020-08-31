# 3d 数据
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)  # 在图上加入 3d 坐标

x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x ** 2 + y ** 2)
z = np.sin(r)

# rstride 和 cstride 分别代表 row 和 column 的跨度。
ax.plot_surface(x, y, z, edgecolor='black', cmap='rainbow', rstride=1, cstride=1)

# offset,映射到那个坐标面长度， zdir：投影方向，可选参数为 [x, y, z] 表示三个轴
ax.contourf(x, y, z, zdir='z', offset=-2, cmap='rainbow')

# 设定 z 轴的取值范围
ax.set_zlim(-2, 2)

plt.show()
