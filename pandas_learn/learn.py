import pandas as pd
import numpy as np

s = pd.Series([1, 2, 6, np.nan, 44.1], index=list(range(2, 7)))
print(s)
print(type(s))

dates = pd.date_range('20190101', periods=6)
print(dates)
print(type(dates))

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
print(type(df))

print(df['b'])
print('--------------')

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)
# a = pd.Series(1, list(range(2, 4)))
# a = pd.Series(1, [2])
# print(a)

df2 = pd.DataFrame({'A': 1,
                    'B': pd.Timestamp('19961024'),
                    'C': pd.Series([1, 2, 3, 4], list(range(4))),
                    'D': np.array([3] * 4, dtype='float32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
print(df2)
print(df2.dtypes)

print(df2.index)
print(df2.columns)
print(df2.values)

print(df2.describe())
print(df2.T)
print(df2.sort_index(axis=1, ascending=False))
print(df2.sort_index(axis=0, ascending=False))

print(df2.sort_values(by='E'))


print(pd.__version__)

