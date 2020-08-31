# numpy 线性代数
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(np.dot(a, b))

print(np.matmul(a, b))

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print(np.dot(a, b))
print(np.inner(a, b))

a = np.arange(10).reshape(2, -1)
print(a)

c = np.where(a > 3)
print(c)
print(np.transpose(np.array(c)))
print(a[c])

print(np.empty((3, 4)))




