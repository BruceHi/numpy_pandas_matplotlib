# 设置坐标轴
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(figsize=(10, 5))


# 设置坐标轴的范围，
plt.xlim(-1, 2)  # plt.xlim((-1, 2)) 这样写也行
plt.ylim(-2, 3)
# 设置轴的标签，轴叫什么名字
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)

# 重新划定刻度，并将刻度起别名，还可以使用 latex 数学美化一下, ‘\ ’ 表示数学公式中的空格
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], r'$bad$, $very\ bad$, normal, good, $y=x^2+b$'.split(', '))

# Get the current:`~matplotlib.axes.Axes 得到当前的轴
ax = plt.gca()

# spines：轴，四周的边框，可选的参数有： ['left', 'right', 'bottom', 'top']
# 设置颜色，默认是没有颜色的
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 脊梁，设置轴的位置，需要填写一个元组位置，元组第一个可以填写 `axes`(比例) 或 `data`（数据点）
# 第二个填写数据，如（`axes`, 0.5）:'center',('data', 0.0):'zero'
ax.spines['bottom'].set_position(('data', 0.0))
ax.spines['left'].set_position(('data', 0.0))

h1, = plt.plot(x, y1, label='line-1')  # 返回一个列表，列表之中只有一个元素，该元素就是 句柄Line2D(line-1)。
h2, = plt.plot(x, y2, color='r', linestyle='--', label='line-2')  # 使用 `h1,` 可以用 h1 提取该元素。


# 可以 用 handles 以及 labels 再改写标签，handeles 里面有一个元素时，只显示一个
# 默认 loc = 'best'
# 'best' : 0,
#  'upper right'  : 1,
#  'upper left'   : 2,
#  'lower left'   : 3,
#  'lower right'  : 4,
#  'right'        : 5,
#  'center left'  : 6,
#  'center right' : 7,
#  'lower center' : 8,
#  'upper center' : 9,
#  'center'       : 10,

plt.legend(handles=[h1, h2], labels=['a', 'b'], loc=1)
plt.show()

# 一般 plot, legend, show 放在后面。
