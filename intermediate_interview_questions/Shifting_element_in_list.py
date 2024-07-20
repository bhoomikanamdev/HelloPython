from collections import deque

# Create a deque object from the list
list_1 = [1, 2, 3, 4, 5, 6]
deque_1 = deque(list_1)

# Rotate the deque by 3 positions to the right
deque_1.rotate(3)

# Convert the deque back to a list
list_1 = list(deque_1)

print(list_1)# Output: [4, 5, 6, 1, 2, 3]