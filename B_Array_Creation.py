import numpy as np

print("Array creation from python list : ")
arr1 = np.array([1,2,3,4])
print(arr1)

print("\n")

print("Array creation using default value : Zeroes method")
arr2 = np.zeros((2,3))
print(arr2)

print("\n")

print("Array Creation using default value : ones method")
arr3 = np.ones((2,3))
print(arr3)

print("\n")

print("Array Creation using specific value : full method")
arr4 = np.full((2,3),7)
print(arr4)

print("\n")

print("Array Creation : arange method")
arr5 = np.arange(1,10,2)
print(arr5)

print("\n")

print("Creating identity matrix : eye method")
arr6 = np.eye(3)
print(arr6)

