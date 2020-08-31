import numpy as np

a = np.arange(10).reshape(2, -1)
print(a)

print(np.where(a > 3))

b = np.array(np.where(a > 3))
print(np.transpose(b))

v = np.zeros(10)
m = np.ones((3, 4))
print(v.shape, m.shape)
print(m.size, m.dtype)

m = np.array([1, 2., 3])
print(m)

print('----------------------')

print(np.linspace(0, 10, 5))

print(np.logspace(1, 10, 10, base=np.e))


print(np.diag([1, 2, 3]))

print(np.diag([1., 2, 3], k=1))

print(np.zeros((3, 3), dtype=int))


print(np.ones((3, 5), dtype=bool))

a = np.linspace(1, 5, 10).reshape((5, 2))
print(a)

m = np.arange(10).reshape(2, 5)
m[m & 1 == 1] = -1
print(m)

m = np.arange(10).reshape(2, 5)
print(m[m & 1 == 1])
print(m[(2 < m) & (m < 7)])  # 注意不能写成链式比较，括号也不能省，也不能换成 and

print(m[m > 2])
print(m[m < 7])

print(m[::-1])

# 进阶部分
print('----------')
v1 = np.arange(10)
print(v1)

v2 = v1.reshape(2, 5)
print(v2)

v2[0][0] = 10
print(v2)

print(v1)
print(v2[:, :4])


a = np.arange(5)
b = np.random.randint(1, 10, (5, 2))
print(np.dot(a, b))

print(np.matmul(a, b))

# 统计变量
print('-----------------')
m = np.random.randint(1, 10, (3, 4))
print(m)

print(np.mean(m))
print(m.mean())
print(m.mean(axis=1))

print(m.sum() / 12)

print(m.std())
print(m.std(axis=1))

print(m.var())
print(m.var(axis=1))

print(m.max())
print(m.max(axis=0))

print(m.min())
print(m.min(axis=1))

print(m.sum())
print(m.sum(axis=1))

print('------------------')
# 累乘
print(m.cumprod())
print(m.cumprod(axis=1))

print(m.cumsum())
print(m.cumsum(axis=0))

# 迹：主对角线之和
print(m.trace())

print(np.array(((1, 2), (3, 4))))

print(np.array([(1, 2), (3, 4)]))

# 改变数组
print('---------------------------')
a = np.random.randint(1, 10, (2, 3))
print(a)

b = a.flatten()
print(b)

b[0] = 30
print(a)
print(b)

a = np.arange(10)
print(a)
print(a[:, np.newaxis])
print(a[:, None])

a = np.array([[1, 2], [3, 4]])
print(a)
print(np.repeat(a, 2, axis=0))
print(np.repeat(a, 2, axis=1))

print('------------------')
# 不管是 vstack，还是 hstack，沿着合并方向的维度，其元素的长度要一致。
b = np.array([[-1, -2]])
print(np.vstack((a, b)))
print(np.vstack((b, a)))
print(np.concatenate((a, b)))

print('--')
b = np.array([[1], [5]])
print(np.hstack((a, b)))
print(np.hstack((b, a)))
print(np.concatenate((a, b), axis=1))

a = np.random.randint(1, 10, (2, 3))
print(a)

print(a.argmax())
print(a.argmax(axis=0))
print(a.argmax(axis=1))



