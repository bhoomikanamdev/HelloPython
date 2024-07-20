'''import pickle

# Object to be pickled
data = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}

# Pickling the object and saving to a file
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)'''

import pickle

    # Unpickling the object from a file
with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
print(data)  # Output: {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}