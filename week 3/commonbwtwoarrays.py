import numpy as np

# Define two arrays
array1 = np.array([1, 2, 3, 4, 5, 6])
array2 = np.array([4, 5, 6, 7, 8, 9])

# Find common values
common_values = np.intersect1d(array1, array2)

# Display results
print("Array 1:", array1)
print("Array 2:", array2)
print("Common Values:", common_values)