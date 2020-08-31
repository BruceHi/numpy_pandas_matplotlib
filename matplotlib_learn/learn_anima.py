# 动画
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i/10))
    return line,  # 返回值是一个元组类型，相当于 return（line,） , 因为函数需要返回一个可迭代类型


def init():
    line.set_ydata(np.sin(x))
    return line,


#
animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=True)

# print(len(init()))

plt.show()

