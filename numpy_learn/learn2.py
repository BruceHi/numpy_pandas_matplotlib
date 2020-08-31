# numpy 创建数组
import numpy as np

# 数组元素为随机值，因为它们未初始化
x = np.empty((3, 2), dtype=int)
print(x)
print(x.dtype)

x = np.zeros(5)
print(x)
x = np.zeros(5, dtype=int)
print(x)

z = np.zeros((2, 2), dtype=[('x', 'i1'), ('y', 'i2')])
print(z)
print(z.dtype)

x = np.ones(5)
print(x.dtype)

z = np.ones(5, dtype=np.int)
print(z)


# 从已有数组创建数组
print('----------------------')
x = [1, 2, 3]
a = np.asarray(x)
print(a)

x = (1, 2, 3)
a = np.asarray(x)
print(a)
print(type(a))

c = np.array(x)
print(c)

x = [(1, 2, 3), (1, 2, 4)]
a = np.asarray(x)
print(a.dtype)

# 这样会报错
# x = [(1, 2, 3), (1, 2)]
# a = np.asarray(x, dtype=int) # 类型指定有毛病
# print(a)

b = np.array(x, dtype=float)
print(b)

x = [1, 2, 3]
a = np.array(x, dtype=float)
print(a)

s = b'Hello, world'
a = np.frombuffer(s, dtype='S1')
print(a)

a = range(5)
b = np.fromiter(a, float)
print(b)

# 从数值范围创建数组
a = np.arange(5)
print(a)

a = np.arange(5, dtype=float)
print(a)

a = np.arange(1., 10, 3)
print(a.dtype)

print('-------------------')

a = np.linspace(1, 10, 10, retstep=True)
print(a)

a = np.linspace(1, 1, 10)
print(a)

a = np.linspace(10, 20, 5)
print(a)

a = np.linspace(10, 20, 5, endpoint=False)
print(a)

b = np.linspace(1, 1, 10).reshape(10, 1)
print(b)

a = np.linspace(1, 2, 10, retstep=True)
print(a)

b = np.logspace(1, 2, 10)
print(b)

a = np.logspace(0, 9, 10, base=2)
print(a)
