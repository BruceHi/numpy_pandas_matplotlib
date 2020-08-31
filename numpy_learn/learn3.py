# 切片与索引
import numpy as np

a = np.arange(10)
print(a)

s = slice(2, 7, 2)
print(a[s])

nums = [1, 2, 3, 4]
s = slice(1, 3)
print(nums[s])
print(type(nums[0]))

b = a[2:7:2]
print(b)

b = a[2]
print(type(b))


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a[1:])

print(a[..., 1])  # 记住是 3 个点加逗号，写成 ： 也是完全可以的

print(a[1, ...])  # 相当于print(a[1])


print(a[..., 1:])

print(a[:, 1:])

# 高级索引, numpy 特有
print('---------------------')

x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

# 布尔索引
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 9]])
print(x[x > 5])

a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])  # nan：not a number
print(a[np.isnan(a)])
print(a[~np.isnan(a)])  # 只能是位的取非 ~，不能是逻辑取非 not，否则会报错


a = np.array([1, 2+3j, 5, 4+3j])
print(a[np.iscomplex(a)])

# 某些花式索引都玩出花来了，还有某些整数数组索引不必掌握，太鸡儿难了。

# 广播
print('--------------------')

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b
print(c)


a = np.array([[0, 0, 0],
              [10, 10, 10],
              [30, 30, 30],
              [40, 40, 40]])
b = np.array([1, 2, 3])
print(a + b)

bb = np.tile(b, (4, 1))
print(a + bb)

a = np.zeros((2, 3))
print(a)

b = np.tile(0., (2, 3))
print(b)

a = np.ones((2, 3))
print(a)

# 可以用 title 表示上面
b = np.tile(1., (2, 3))
print(b)

# 迭代数组
print('-----------------')

a = np.arange(6).reshape(2, 3)
print(a)

for x in a:  # 迭代最底层数组
    print(x, end=' ')
print()

for x in np.nditer(a):  # 迭代每一个元素，一行一行展开显示
    print(x, end=' ')
print()

a = np.arange(6).reshape(2, 3)
print(a)

for x in a.T:
    print(x, end=' ')
print()

for x in np.nditer(a.T):  # 遍历 a 的转置，与 遍历 a 得到了同样的结果，说明在内存中的存储顺序一样。
    print(x, end=' ')
print()

for x in np.nditer(a.T.copy(order='C')):  # 强制按 行 展开
    print(x, end=' ')
print()

a = np.arange(0, 60, 5).reshape(3, 4)
print(a)

# 遍历的同时修改元素的值，还是理解就好，知道有这个东西
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x

print(a)

a = np.arange(0, 60, 5).reshape(3, 4)
b = np.array([1, 2, 3, 4])
for x, y in np.nditer((a, b)):
    print('%d:%d' % (x, y), end=' ')
print()

for x in np.nditer((a, b)):
    print(x, end=' ')
print()











