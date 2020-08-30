# Data Types in NumPy
import numpy as np
print("<-- Data Types in Numpy -->")
"""
	1.)  i-> integer             2.)  b-> boolean          3.) u-> unsigned integer
	4.)  f-> float             	 5.)  c-> complex float    6.) m-> timedelta
	7.)  M-> datetime          	 8.)  O-> Object           9.) S-> String
	10.) U-> unicode string      11.) V-> fixed chunk of memory for other type(void)
"""
# checking the Data Type of an array:-
print("<-- Checking Data Type of an array -->")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr.dtype)

arr1 = np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype)

arr2 = np.array([1, 2, 3, 4, 5], dtype="S")
print(arr2)
print(arr2.dtype)

myarr = np.array([1, 2, 3, 4], dtype='i4')
print(myarr)
print(myarr.dtype)

# Converting data type on existing array
print("<-- converting data type on existing array -->")
arr3 = np.array([1.1, 2.2, 3.2, 4.5])
newarr = arr3.astype("i")
print(newarr)
print(newarr.dtype)

newarr1 = arr3.astype("int")
print(newarr1)
print(newarr1.dtype)

arr4 = np.array([1, 0, 3, 0, 5])
newarr3 = arr4.astype("bool")
print(newarr3)
print(newarr3.dtype)
