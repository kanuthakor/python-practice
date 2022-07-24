from numpy import *

#array one
arr1 = array([1,23,12,43,12,55])
print(arr1)

#array two
arr2 = array([56,46,32,54,67,45])
print(arr2)

#declaration of array with initial values be zero
arr_sum = zeros(6,int)

#adding two arrays using for loop
for i in range(0,6):
    arr_sum[i] = arr1[i] + arr2[i]

print(arr_sum)
