
import numpy as np

# Create a NumPy array of random integers
arr = np.random.randint(0, 100, size=10)

# Sort the array in ascending order
arr_sorted = np.sort(arr)

print(arr)         # [47 28 56 21 75 24 51 16 29 86]
print(arr_sorted)  # [16 21 24 28 29 47 51 56 75 86]
