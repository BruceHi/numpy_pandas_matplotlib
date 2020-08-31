# pandas 设置值
import pandas as pd
import numpy as np

dates = pd.date_range('20200405', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), dates, columns=['A', 'B', 'C', 'D'])
print(df)

df.iloc[2, 2] = 11111
print(df)

df.loc['20200406', 'B'] = 66666
print(df)

# df[df.A > 8] = 0
# print(df)

df.B[df.A > 8] = 0
print(df)

df['F'] = np.nan  # 新添加一列，并赋值 nan
print(df)

# df['E'] = pd.Series([1, 2, 3, 4, 5, 6, 7])  # 必须指定序列，否则添加的全为 nan
# # # print(df)

# new = pd.DataFrame(np.arange(12).reshape((3, 4)))
# print(new)
# new['e'] = pd.Series([333, 444, 555, 'dd'])  # 多出来的长度被截断，默认序列是从 0 开始的，那就不用特别指定了。
# print(new)

df['E'] = pd.Series([1, 2, 3, 4, 5, 6], pd.date_range('20200406', periods=6))  # **序列不符合的直接填充 nan**
print(df)



