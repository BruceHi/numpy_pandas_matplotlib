# 合并 merge，针对两个进行合并，没有 axis，必须要给出按什么合并（列）
import pandas as pd
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)

res = pd.merge(left, right, on='key')
print(res)

print('----------')
# 根据两组 key 进行合并
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)

# how 的取值 ['left', 'right', 'outer', 'inner'], 默认 inner
print(pd.merge(left, right, on=['key1', 'key2']))
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))
print(pd.merge(left, right, on=['key1', 'key2'], how='left'))
print(pd.merge(left, right, on=['key1', 'key2'], how='right'))
print(pd.merge(left, right, on='key1'))


print('-----------')
# 使用 indicator
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
print(pd.merge(df1, df2, indicator=True))
print(pd.merge(df1, df2, how='outer', indicator=True))  # 打印合并方式, indicator 是 bool 类型，不允许乱改名
print(pd.merge(df1, df2, how='outer', indicator='indicator_column'))  # 打印合并方式，并改名，最好不要改

print('----------')
# 依据 index 合并
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
print(left)
print(right)

# 必须左右索引都要设置成 True
# 否则 pandas.errors.MergeError: Must pass right_on or right_index=True
print(pd.merge(left, right, left_index=True, right_index=True, how='outer'))
print(pd.merge(left, right, left_index=True, right_index=True))


# 使用 suffix 解决overlapping的问题
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
print(pd.merge(boys, girls, on='k'))  # 这里会自己起名，age_x  age_y
print(pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl']))  # 指定名字

