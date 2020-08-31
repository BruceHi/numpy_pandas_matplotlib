# 选择
import pandas as pd
import numpy as np

dates = pd.date_range('20200708', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
print(df['A'])  # 列，只能选择一列，不能选择多列
# print(df['20200708'])  # 错误，self.columns.get_loc(key)，默认一个元素当成列标签。

# 根据标签选择
print(df['20200708': '20200709'])  # 正确，选择两行
print(df['20200708': '20200708'])  # 正确，选择1行

print(df[1: 3])  # 行
# print(df[1])  # 错误，不能直接这样写，会把 1 当成标签 key 的
# print(df[1,])  # 只要里面没有 ：都会当成标签。
print('----------')
#
# new = pd.DataFrame(np.arange(4, 5), columns=)


# 列
print(df.columns[1:4])
print(df[df.columns[1:4]])

print('------')
#
# new = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=['a', 'b', 'c'])
# print(new)
#
# print(new[1:2])  # 只会当成切片


# 根据标签
print(df)
print(df.loc['20200710'])
print(df.loc[['20200708', '20200713']])  # 列可以省略，行不能
print(df.loc[:, ['A', 'C']])
print(df.loc['20200712', ['A', 'C']])
print('---------')

# 根据序列
print(df)
print(df.iloc[0, 0])
print(df.iloc[2:4])  # 列可以省略，行不能
print(df.iloc[[1, 3, 4], 2:3])
print(df.iloc[2:4, 2:3])

# 根据判断
print(df[df.A > 12])

print('------')
data = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list(range(3)))
print(data)
print(data[1])  # 一个元素就是列标签的意思
print(data[1:2])  # 行，按照索引选，必须有 ：。


## 总结
# data[] 列元素是根据标签选的，并且只能选择一列。self.columns.get_loc(key)，默认一个元素当成列标签。
# 行元素可以根据索引（切片）及索引标签选择：前者类似切片，不包括结束区间，后者包含结束区间。
# 必须要有 ：，以明示这是行的选取。不能写成**单个索引或切片**，单个的系统会当成 key，对比列。
