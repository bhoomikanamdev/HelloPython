import pandas as pd

# Create example DataFrame
data = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Alice'],
    'Department': ['HR', 'Finance', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 60000, 70000, 50000]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Unique values in the 'Name' column
unique_names = df['Name'].unique()
print("\nUnique values in the 'Name' column:")
print(unique_names)

# Unique values in the 'Department' column
unique_departments = df['Department'].unique()
print("\nUnique values in the 'Department' column:")
print(unique_departments)

# Count of unique values in the 'Name' column
unique_names_count = df['Name'].nunique()
print("\nCount of unique values in the 'Name' column:")
print(unique_names_count)

# Count of unique values in the 'Department' column
unique_departments_count = df['Department'].nunique()
print("\nCount of unique values in the 'Department' column:")
print(unique_departments_count)

# Unique values for multiple columns
for column in ['Name', 'Department']:
    unique_values = df[column].unique()
    print(f"\nUnique values in the '{column}' column:")
    print(unique_values)

# Count of unique values for all columns
unique_counts = df.nunique()
print("\nCount of unique values for all columns:")
print(unique_counts)


