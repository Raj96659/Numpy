import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print("Vertical Stack : ")
print(np.vstack((arr1,arr2)))

print("\n")

print("Horizontal Stack : ")
print(np.hstack((arr1,arr2)))

print("\n")

# Spliting

arr3 = np.array([10,20,30,40,50,60])
print("Spliting : ")
print(np.split(arr3,2))

