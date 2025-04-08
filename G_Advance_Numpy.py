import numpy as np

arr = np.array([22,23,24,25])

new_arr = np.insert(arr,2,30)

print("Numpy array after inserting 30 : ")
print(new_arr)

print("\n")

arr_2d = np.array([[1,2,3],[4,5,6]])

new_arr_2d = np.insert(arr_2d,1,[7,8,9],axis=0)
print("Numpy array after inserting [7,8,9] at index 1 and axis 0 : ")
print(new_arr_2d)

print("\n")

arr2 = np.array([10,20,30])
new_arr2 = np.append(arr2,[40,50,60])
print("Numpy Array after appending [40,50,60] : ")
print(new_arr2)

print("\n")

arr3 = np.array([1,2,3])
arr4 = np.array([4,5,6])

new_arr3 = np.concatenate((arr3,arr4))
print("Numpy array after concatenation is : ")
print(new_arr3)

print("\n")

arr5 = np.array([10,20,30,40,50,60])

new_arr4 = np.delete(arr5,2)
print("Numpy array after deleting the elemnet at index 2 which is 30 : ")
print(new_arr4)

print("\n")

arr6_2d = np.array([[11,12,13],[14,15,16]])
new_arr5_2d = np.delete(arr6_2d,0,axis=0)
print("Numpy array after deleting the element [11,12,13] : ")
print(new_arr5_2d)

print("\n")
