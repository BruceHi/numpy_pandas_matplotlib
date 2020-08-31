import numpy as np

a = np.arange(10).reshape(2, 5)
b = np.array([2])
print(a + b)

b = np.tile(2, (2, 5))
print(a + b)

# b = np.array([1, 2])
# print(a + b)

a = np.arange(6).reshape((2, 1, 3))  # 最好维数是3 以及以上的就上 （）
b = np.arange(12).reshape(4, 3)  # a.reshape(10, 11) = a.reshape((10, 11)) 官方示例
print(a)
print(b)
print('--------')
print(a + b)

# a = np.repeat(a, 4, axis=1)
# print('a: repeat', np.repeat(a, 4, axis=1))
# print('a: tail', np.tile(a, (1, 4, 1)))

# b = b[np.newaxis, :, :]
# print(b)
# b = np.repeat(b, 2, axis=0)
# print(b)
#
# print(a + b)

# numpy 练习题
print('------------------------')
#


# b = a.repeat(3, axis=1)
# b = a.repeat(3, axis=0)

a = np.array([[1, 2], [3, 4]])

print(a.repeat(3))
print(a.repeat(3, axis=0))
print(a.repeat(3, axis=1))
print('---')
print(np.tile(a, 3))
print(np.tile(a, (1, 3)))
print(np.tile(a, (3, 1)))

print('-----------------------------')

a = np.array([1, 2, 3])
print(a.repeat(3))
print(np.tile(a, 3))

b = np.hstack((a.repeat(3), np.tile(a, 3)))
print(b)


a = np.random.randint(1, 10, (2, 4, 3))
print(a)
ma = np.median(a, axis=1)
print(ma)

print('----------------')
a = np.array([0., 1, np.nan, 3, np.nan, np.nan, 6, 7, 8, 9])
print(np.where(np.isnan(a)))
print(a[np.where(np.isnan(a))])

# 返回无缺失值的行
a = np.array([[ 0., np.nan,  2.,  3.],
       [ 4.,  5., np.nan,  7.],
       [ 8.,  9., 10., 11.],
       [12., 13., np.nan, 15.],
       [16., 17., np.nan, 19.],
       [20., 21., 22., 23.]])
m = np.sum(np.isnan(a), axis=1) == 0  # 牛批, m 的值是 bool 类型
print(m)
print(a[m])

a[np.isnan(a)] = 0  # 把缺失值（nan）替换成 0
print(a)


print(True + True)


