import numpy as np

# 数组操作
a = np.arange(9).reshape(3, 3)
print(a)

for e in a.flat:
    print(e, end=' ')
print()

print(a.flatten())

print(a.flatten(order='F'))

print(np.ravel(a))

# 转置
print(np.transpose(a))
print(a.T)

# 连接
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.concatenate((a, b))  # 默认是按 0 轴链接，既纵轴
print(c)

c = np.concatenate((a, b), 1)
print(c)

# 添加
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.append(a, [7, 8, 9, 10]))  # axis 不写的话，默认是拍平，然后连接

print(np.append(a, [[7, 8, 9], [7, 8, 9]], 0))  # 维度要匹配，不然出错
print(np.append(a, [[1, 2], [3, 4]], axis=1))


# 数学函数
print('------------------')

a = np.array([1.0, 4.67, 5.55, 9.1])
print(np.around(a))  # 四舍五入，而普通的 round 不完全符合四舍五入

a = np.array([-1.7, 1.5, -0.2, 10.3])
print(np.floor(a))

print(np.ceil(a))

a = np.arange(9.).reshape(3, 3)
print(a)

b = np.array([10, 10, 10])
print(np.add(a, b))

print(np.subtract(a, b))
print(np.multiply(a, b))  # 针对的是可以进行广播的，数组形状不变
print(np.divide(a, b))

a = np.array([10, 100, 1000])
b = np.array([1, 2, 3])
print(np.power(a, 2))
print(np.power(a, b))

a = np.array([10, 20, 30])
b = np.array([3, 5, 7])
print(np.mod(a, 2))
print(np.mod(a, b))

print('-------------------')
# 统计函数
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print(a)

print(np.amin(a))
print(np.amin(a, axis=0))  # 纵向比较，相当于沿纵轴压缩数据
print(np.amin(a, axis=1))

print(np.amax(a))
print(np.amax(a, axis=0))
print(np.amax(a, axis=1))


# 中位数
print(np.median(a))

print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

print('------------')
# 加权平均
a = np.array([1, 2, 3, 4])
print(np.average(a))
b = np.array([5, 6, 7, 8])
print(np.average(a, weights=b))
print(np.average(a, weights=b, returned=True))

print(np.std([1, 2, 3, 4]))
print(np.var([1, 2, 3, 4]))

# 排序
a = np.array([[3, 7], [9, 1]])

print(np.sort(a))

print(np.sort(a, axis=1))
print(np.sort(a, axis=0))


a = np.array([[30, 40, 50], [80, 20, 10], [50, 90, 60]])
print(np.argmax(a))
print(np.argmax(a, axis=0))
print(np.argmax(a, axis=1))

min_dex = np.argmin(a)
print(a.flatten()[min_dex])

print('----------------------')
# 条件筛选
x = np.arange(9.).reshape(3, 3)
print(x)
y = np.where(x > 4)  # 返回索引
print(y)
print(x[y])

a = np.arange(12).reshape(3, 4)
print(a)
print(a.T)
print(type(a.T))


import numpy.matlib
print(np.matlib.empty((2,2)))

print(type(np.matlib.empty((2,2))))

print(np.__version__)


