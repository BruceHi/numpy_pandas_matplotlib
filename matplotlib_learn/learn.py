import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()  # 默认从编号 1 开始的。
plt.plot(x, y1)

plt.figure(num=3, figsize=(8, 5))  # 设置长度、宽度
plt.plot(x, y1, label='line 1')
plt.plot(x, y2, color='y', marker='.', linestyle='--', linewidth=2, label='line 2')

# marker 是标记点的意思，出现的点进行标记。
# color 颜色。
# linestyle 线段风格，比如虚线实线等。
# linewidth：线段宽度，默认是 1
# label 要配合 plt.legend（图例） 使用，会在下方标注某种线段叫什么 label，如叫 line2。

plt.legend()
plt.show()


