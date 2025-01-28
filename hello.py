print('loading specific libraries')
import pandas as pd
print('Hello World')
df1 = pandas.DataFrame({'a': [1, 3, 4], 'b': [5, 3, 1]}, columns = ['a', 'b'])
df2 = pandas.DataFrame({'b': [5, 2, 0], 'a': [1, 2, 8]}, columns = ['b', 'a'], index = [2, 1, 0])
print(df1 + df2)

print('Créer un dataframe échantillon')
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)
 
print('Créer un tracé de ligne')
df.plot()

