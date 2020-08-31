import numpy as np
print(np.eye(4))

a = np.array([1, 2, 3])
print(a)

# 结果： [list([1, 2]) list([3])]
# a = np.array([[1, 2], [3]])  # 不推荐，这种是粗糙的创建方式。
# print(a)


a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)

a = np.array([1, 2, 3], dtype=complex)
print(a)


print(2 * [1, 2])
print(2 * np.array([1, 2]))  # 广播？

print('------------------------------')
# numpy 数组类型
dt = np.dtype(np.int32)
print(dt)

dt = np.dtype('i4')
print(dt)

dt = np.dtype('<i4')
print(dt)

dt = np.dtype([('age', np.int8)])
print(dt)

a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)
print(a.dtype)

dt = np.dtype('i4')
b = np.array([1, 2, 3], dtype=dt)
print(b)
print(b.dtype)
print(type(b))

dt = np.dtype([('age', np.int8)])
a = np.array([(24, ), (40, ), (23, )], dtype=dt)
print(a.dtype)
print(a['age'])

# 必须是 大写 S20
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
a = np.array([('abc', 21, 50.0), ('xyz', 18, 75.0)])
print(a)

# IndexError: only integers, slices (`:`), ellipsis (`...`),
# numpy.newaxis (`None`) and integer or boolean arrays are valid indices
# print(a['name'])

# 数组属性
print('-------------------')

a = np.arange(24)
print(a.ndim)
b = a.reshape((2, 3, 4))  # 2 * 3 * 4 = 24
print(b.ndim)

a = np.array([[1, 2, 3], [2, 3, 4]])
print(a.shape)

a = np.array([[1, 3, 4], [4, 5, 6]])
a.shape = 3, 2
a.shape = (3, 2)
print(a)

print('---------------')
b = a.reshape(2, 3)  # reshape 其实还是原始数组的视图，改变它的值，原始数组也会改变
b[0][0] = 10000
print(b)
print('a', a)


x = np.array([1, 2, 3])
print(x.itemsize)  # 4 个字节，32位

y = np.array([1, 2, 3], dtype='i1')
print(y.itemsize)

y = np.array([1, 2], dtype=np.float)
print(y.itemsize)
print(y.flags)
