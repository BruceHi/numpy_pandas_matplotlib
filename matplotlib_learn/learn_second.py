# 次坐标轴
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x ** 2
y2 = -y1

fig, ax1 = plt.subplots()

ax1.plot(x, y1, 'g')
ax1.set_xlabel('x data')
ax1.set_ylabel('y1 data', color='g')

# 生成一个新的轴，x 轴共享
ax2 = ax1.twinx()
ax2.plot(x, y2, 'r')
ax2.set_ylabel('y2 data', color='r')

plt.show()
