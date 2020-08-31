# 多图合一显示
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

# 2 行 2 列 第一个图
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 2])

# 可以简写
plt.subplot(223)
plt.plot([0, 1], [0, 3])

plt.subplot(224)
plt.plot([0, 1], [0, 4])


# 一个大图，三个小图
plt.figure()

plt.subplot(211)
plt.plot([0, 1], [0, 3])

# 注意要从 4 开始
plt.subplot(234)
plt.plot([0, 1], [0, 2])

plt.subplot(235)
plt.plot([0, 1], [0, 3])

plt.subplot(236)
plt.plot([0, 1], [0, 4])

plt.show()
