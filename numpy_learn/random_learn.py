# random：生产伪随机数
import string
import random

# 生产随机密码
# a = int(input('请输入密码的长度:\n'))
# b = string.digits + string.ascii_letters + string.punctuation
#
# password = ''
# for _ in range(a):
#     password += random.choice(b)
# print(password)

print('从 0 到 100 中选取一个奇数：', random.randrange(1, 100, 2))
print(random.randrange(100))

print(random.random())  # 无参，返回 [0, 1)

print('------')
# 初始化随机种子
random.seed()
print(random.random())
print(random.random())

# 使用了相同的随机种子 10，生产的随机数也是一样的。
random.seed(10)
print(random.random())

random.seed(10)
print(random.random())

a = [20, 16, 10, 15]
random.shuffle(a)
print(a)

a = [20, 16, 10, 15]
random.shuffle(a)
print(a)

print(random.uniform(3, 5))
print(random.uniform(5, 3))

# https://docs.python.org/zh-cn/3.7/library/random.html
# 基本示例看懂就 ok 了。

print(random.randint(3, 4))
print(random.randint(3, 4))
print(random.randint(3, 4))
print(random.randint(3, 4))
print(random.randint(3, 4))
print(random.randint(3, 4))
print(random.randint(3, 4))
print(random.randint(3, 4))


a = [1, 4, 5, 2, 4, 5]
print(random.sample(a, k=5))
print(random.sample(a, k=6))

random.shuffle(a)
print(a)


