# image 图片
import matplotlib.pyplot as plt
import numpy as np

a = np.random.rand(9).reshape(3, 3)
# print(a)

# interpolation：插补，origin：表示是否上下反过来，可选参数为 upper、lower
plt.imshow(a, interpolation='nearest', cmap='gray', origin='lower')
# 图示说明，长度变为原来 0.8 倍
plt.colorbar(shrink=0.8)


plt.xticks([])
plt.yticks([])
plt.show()
