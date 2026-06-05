import numpy as np

arr = np.array([40, 10, 30, 20, 50, 20, 30])

print("Original Array:")
print(arr)

print()

print("Sorted Array:")
print(np.sort(arr))

print()

print("Index of 30:")
print(np.where(arr == 30))

print()

print("Unique Values:")
print(np.unique(arr))