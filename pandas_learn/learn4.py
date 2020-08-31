# 处理丢失数据
import pandas as pd
import numpy as np

dates = pd.date_range('20200102', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)

print(df.dropna(axis=0, how='any'))  # how = {'any', 'all'}  纵向操作，横轴长度不变
print(df.dropna(axis=1, how='any'))

print(df.fillna(0))

print('-----------------')

print(df.isna())  # 两个相等
print(df.isnull())

print(any(df.isnull()))

# 读取 csv
data = pd.read_csv('student.csv')
print(data)

data.to_pickle('student.pickle')

