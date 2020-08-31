import numpy as np
import collections

# a = np.random.random((3, 4))
a = np.arange(12, 0, -1).reshape(3, 4)
print(a)

print(np.diff(a))
print(np.sort(a))  # 默认 axsi=-1

# 限制最小最大值
print(np.clip(a, 5, 10))
for val in a.flat:
    print(val)

print(isinstance(a.flat, collections.Iterator))

# b = [[1, 2, 3], [1, 5, 6]]
# for row in b:
#     print(row)
# for column in zip(*b):
#     print(list(column))

a = np.array([[1, 2, 3]])
b = np.array([1, 2, 3])
print(a.shape, b.shape)

print(b[None, :].shape)  # 横轴加了一个维度
print(b[:, np.newaxis].shape)
print(b[:, np.newaxis])

print('-----------')
# 分隔
a = np.arange(12).reshape(3, 4)
print(a)
print(np.split(a, 2, axis=1))
print(np.split(a, 3))  # 默认 axis=0

print(np.array_split(a, 3, axis=1))  # 默认 axis=0，不等量分隔，一般最后一个剩余的少
print(np.vsplit(a, 3))  # 纵向
print(np.hsplit(a, 2))  # 横向

print(a)
print(a[:2, 1])
c = a[:]  # numpy 的切片是原数组的引用
a[0, 0] = 445
print(a)
print(c)

# # python 中的切片会产生新的列表
# d = [1, 2, 3]
# c = d[:]
# d[0] = 5
# print(c)
# print(d)

d = a.copy()  # 拷贝（深拷贝）
d[0][0] = 1000
print(a)
print(d)



