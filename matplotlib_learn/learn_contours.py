# 等高线
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 255)
y = np.linspace(-3, 3, 255)

# 生成网格，返回list,有两个元素,第一个元素是X轴的取值,第二个元素是Y轴的取值
X, Y = np.meshgrid(x, y)


def f(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)


# 填充颜色：8 代表分割线，热线图：hot，冷线图：cool
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap='hot')

# 划线：colors，linewidths 不要忘记 有s
c = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidths=0.5)

# 添加高度数字，inline：穿过数字那些地方留空白
plt.clabel(c, inline=True, fontsize=10)


# 列出所有可用等高线图的颜色
# print(list(plt.cm.cmap_d.keys()))
# print(len(plt.cm.cmap_d.keys()))


plt.xticks([])
plt.yticks([])

plt.show()


