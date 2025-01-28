print('loading specific libraries')
import pandas as pd
import numpy as np
import os

print('settings')
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)


print('Create df1')
df1 = pd.DataFrame({'a': [1, 3, 4], 'b': [5, 3, 1]}, columns = ['a', 'b'])
print(df1)
#df1_string = df1.to_csv(index=False)
#os.environ['RESULT'] = df1_string  # Store in environment variable
#df2 = pd.DataFrame({'b': [5, 2, 0], 'a': [1, 2, 8]}, columns = ['b', 'a'], index = [2, 1, 0])
#print(df1 + df2)

print('Créer un dataframe échantillon')
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)
 
print('Créer un tracé de ligne')
#df.plot()

