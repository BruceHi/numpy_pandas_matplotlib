# 散点图
import matplotlib.pyplot as plt
import numpy as np

n = 1024
x = np.random.normal(size=1024)
y = np.random.normal(size=1024)
print(x)
t = np.arctan2(y, x)

# s: size 大小的意思, c：color 颜色为 t, alpha：透明度
plt.scatter(x, y, s=75, c=t, alpha=0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# 把刻度置为 空
plt.xticks([])
plt.yticks([])

plt.show()
