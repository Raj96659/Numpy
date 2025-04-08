import numpy as np

arr = np.array([10,np.nan,30,np.nan,50])
print("Check the null values : ")
print(np.isnan(arr))

print("\n")

print("Fill the nan value with 7 : ")
cleaned_arr = np.nan_to_num(arr,nan=7)
print(cleaned_arr)
