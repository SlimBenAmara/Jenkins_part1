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

# Check if the environment variable is properly retrieved
if df_string:
    # Clean up any extra whitespace or newlines
    df_string = df_string.strip()
    
    # Convert the CSV string back to a DataFrame using StringIO
    try:
        df2 = pd.read_csv(StringIO(df_string))
        print("Retrieved DataFrame:")
        print(df2)
    except Exception as e:
        print(f"Error reading CSV: {e}")
else:
    print("RESULT environment variable is not set.")

df1_ = pd.DataFrame({'a': [1, 3, 4], 'b': [5, 3, 1]}, columns = ['a', 'b'])


if 'df1_' in locals() and 'df2' in locals():
    print(df1_ + df2)
else:
    print("df1_ or df2 is not defined properly.")
