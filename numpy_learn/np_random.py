import numpy as np


print(np.random.rand(3, 3))
print(np.random.rand(3, 3))

np.random.seed(5)
print(np.random.rand(3, 3))

np.random.seed(5)
print(np.random.rand(3, 3))

print(np.random.rand())
print(type(np.random.rand()))
print(np.random.rand(1))
print(type(np.random.rand(1)))


a = np.random.randn(3, 3)
print(a)

print(np.mean(a, axis=0))
print(np.std(a))
print(np.var(a))

print('----------')
print(np.random.randint(1, size=10))

print(np.random.randint(4, 6))
print(np.random.randint(4, 6))

print(np.random.randint(4, 6))
print(np.random.randint(4, size=1))


print(np.random.random_sample())

print(np.random.random_sample([3, 2]))
print(np.random.random((3, 4)))


print(np.random.choice(5))
