# 柱状图
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y1 = (1 - x/float(12)) * np.random.uniform(0.5, 1.0, 12)
y2 = (1 - x/float(12)) * np.random.uniform(0.5, 1.0, 12)

plt.xlim(-0.5, 12)
plt.ylim(-1.25, 1.25)

# plt.figure(3)  # 加上这一句，就默认产生 figure 1，以及 figure 3 这两个图，第一个图只有刻度
plt.bar(x, +y1, facecolor='green', edgecolor='white')
plt.bar(x, -y2, edgecolor='white')

for a, b in zip(x, y1):
    # ha:horizontal 对齐
    # va ：vertical 对齐
    plt.text(a, b+0.05, '%.2f' % b, ha='center', va='bottom')

for a, b in zip(x, y2):
    plt.text(a, -b-0.05, '%.2f' % b, ha='center', va='top')

plt.show()
