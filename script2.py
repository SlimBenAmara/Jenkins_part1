print('loading specific libraries')
import pandas as pd
import os
from io import StringIO

print('settings')
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)


# Retrieve the environment variable (CSV string)
df_string = os.environ.get('RESULT')




print('Create second dataframe : df2')
#df2 = pd.DataFrame({'b': [5, 2, 0], 'a': [1, 2, 8]}, columns = ['b', 'a'], index = [2, 1, 0])

# Check if the environment variable is properly retrieved
if df_string:
    # Convert the CSV string back to a DataFrame
    df2 = pd.read_csv(StringIO(df_string))
    print("Retrieved DataFrame:")
    print(df2)
else:
    print("RESULT environment variable is not set.")


# if 'df1' in locals() and 'df2' in locals():
#     print(df1 + df2)
# else:
#     print("df1 or df2 is not defined properly.")
