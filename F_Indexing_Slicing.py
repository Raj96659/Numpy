import numpy as np

arr = np.array([21,22,23,24,25,26])

print(arr[1])
print(arr[-1])
print(arr[1:4])

# fancy indexing
print(arr[[1,3,5]])

#filtering

print(arr[arr > 23])
