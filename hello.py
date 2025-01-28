print('loading specific libraries')
import pandas as pd
import numpy as np
import os

print('settings')
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)


print('Create df1')
# Create a DataFrame
df1 = pd.DataFrame({'a': [1, 3, 4], 'b': [5, 3, 1]}, columns=['a', 'b'])

# Convert the DataFrame to CSV format (as a string) and print it
df_string = df1.to_csv(index=False)
print(df_string)  # Ensure that only the CSV string is printed
