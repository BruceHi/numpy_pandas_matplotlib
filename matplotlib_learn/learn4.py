# tick（轴上的分隔点） 能见度
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

# alpha：透明度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='None', zorder=2))

# zorder 表示图层顺序，数值最大的在顶层
plt.plot(x, y, linewidth=10, zorder=1)

plt.show()

