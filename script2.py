print('loading specific libraries')
import pandas as pd


print('settings')
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)


print('Hello World')

df2 = pd.DataFrame({'b': [5, 2, 0], 'a': [1, 2, 8]}, columns = ['b', 'a'], index = [2, 1, 0])
print(df1 + df2)
