# Subplot 分格显示
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

plt.figure()

# 3行3列, (0,0)表示从第0行第0列开始作图，
# colspan=3表示列的跨度为3, rowspan=1表示行的跨度为1. colspan和rowspan缺省, 默认跨度为1
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)

# 原来的 plt 要换为 ax1，属性设置前面要加 set_
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1_title')

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')


ax5 = plt.subplot2grid((3, 3), (2, 1))


# 另一种显示方法
plt.figure()
gs = gridspec.GridSpec(3, 3)
plt.subplot(gs[0, :])
plt.subplot(gs[1, :2])
plt.subplot(gs[1:, 2])
plt.subplot(gs[2, 0])
plt.subplot(gs[2, 1])

# 第三种方法, 不要另起 figure
# plt.figure()

# 默认：Create just a figure and only one subplot
# 2 行 2 列，是否共享 x 轴坐标，是否共享 y 轴坐标，True = 'all', False = 'none'
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex='all', sharey='all')
ax11.scatter([1, 2], [1, 2])
# 紧凑布局
plt.tight_layout()


plt.show()