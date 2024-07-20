import pandas as pd

# Example DataFrame
data = {
    'A': ['foo', 'bar', 'baz', 'qux'],
    'B': [5, 15, 10, 20],
    'C': [100, 200, 300, 400]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Create boolean mask based on condition (B > 10)
condition = df['B'] > 10

# Set 'A' as index where condition is True
df_indexed = df[condition].set_index('A')

print("\nIndexed DataFrame based on condition (B > 10):")
print(df_indexed)

