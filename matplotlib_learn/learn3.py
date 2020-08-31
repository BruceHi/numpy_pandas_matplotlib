# 标注
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.xlim(-3, 3)
plt.ylim(-6, 8)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
plt.plot(x, y)

# 绘制一个点
x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, color='b')
# 线段
plt.plot([x0, x0], [0, y0], 'r--')

plt.annotate('r', xy=(x0, y0), xytext=(5, -5), textcoords='offset points')
# 基于坐标轴位置
plt.text(0, 1, 'hello')

plt.show()
