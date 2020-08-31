# 连接 concat：concatenation
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)), columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
print(df1)

res = pd.concat([df1, df2, df3])  # 默认 axis=0
print(res)

print(pd.concat([df1, df2, df3], ignore_index=True))

print('----------')
df4 = pd.DataFrame(np.ones((3, 4)) * 0, index=[1, 2, 3], columns=['a', 'b', 'c', 'd'])
df5 = pd.DataFrame(np.ones((3, 4)), index=[2, 3, 4], columns=['b', 'c', 'd', 'e'])
print(pd.concat([df4, df5]))  # 默认 join 为 outer，空位置补 nan

print(pd.concat([df4, df5], join='inner', ignore_index=True))

# 横向合并，注意 join_axis 已经被移除
print(pd.concat([df4, df5], axis=1))
print(pd.concat([df4, df5], axis=1, join='inner'))

# append 只能用于 纵轴添加
print(df1.append(df2, ignore_index=True))
print(df1.append([df2, df3]))

print(df4.append([df2, df5]))  # 纵轴，‘outer'
print(pd.concat([df1, df2, df5]))  # 与上面的那个相等


