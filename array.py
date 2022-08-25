import numpy as np # Import numpy library
my_lst=[1,2,3,4,5]
arr=np.array(my_lst) # Converting list to array
print(type(arr)) # Checking type of array
print(arr)
print(arr.shape) # Checking dimension of array

## Multi-nested array
my_lst1=[3,5,4,6,7]
my_lst2=[3,4,6,7,9]
my_lst3=[1,4,6,8,9]

arr1=np.array([my_lst1,my_lst2,my_lst3]) #Converting to two dimension array
print(arr1)
print(arr1.shape) # Checking dimension of array

print(arr1.reshape(5,3)) # Reshaping the array 

## Indexing
print(arr[3]) # Indexing in single dimension array
print(arr1[0:2,1:3]) # Indexing in two dimension array [0:2-top to bottom/row; 1:3-left to right/column]









