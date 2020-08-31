# pandas plot 画图
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000))
print(data)

data = data.cumsum()  # 累加
print(data)

# data.plot()
# plt.show()

data = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))
print(data)

data = data.cumsum()
# data.plot()
# plt.show()

ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='class1')
data.plot.scatter(x='A', y='C', color='LightGreen', label='class2', ax=ax)
plt.show()
