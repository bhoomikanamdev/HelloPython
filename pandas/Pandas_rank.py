

import pandas as pd

# Step 1: Create a DataFrame using a list of data and list of columns
data = [
    {'Name': 'Alice', 'Age': 23, 'Department': 'HR'},
    {'Name': 'Bob', 'Age': 35, 'Department': 'IT'},
    {'Name': 'Charlie', 'Age': 45, 'Department': 'Finance'},
    {'Name': 'David', 'Age': 29, 'Department': 'HR'},
    {'Name': 'Eva', 'Age': 41, 'Department': 'IT'},
]

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Step 2: Add a new row number column to the DataFrame
df.insert(0, 'RowNumber', range(1, len(df) + 1))
print("\nDataFrame with RowNumber:")
print(df)

# Step 3: Add a rank column using grouping of another column values
df['Rank'] = df.groupby('Department')['Age'].rank(method='dense')
print("\nDataFrame with Rank by Age within each Department:")
print(df)