# 图中图
import matplotlib.pyplot as plt


x = range(1, 8)
y = [1, 3, 4, 2, 5, 8, 6]

fig = plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.title('title1')
plt.plot(x, y)


left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax = fig.add_axes([left, bottom, width, height])
ax.plot(y, x, 'r')
# 前面要加 set_
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title inside 1')

# 第二种方法，建议使用第二种方法
# 下面所有的都归 axes 位置管
# left, bottom, width, height
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')


plt.show()
