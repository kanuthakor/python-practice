from numpy import *

#creating an array
arr = array([1,2,3,5,2,36,7,3])

#assigning one value to maximum variable
maximum = arr[0]

#finding maximum value
for num in arr:
    if num > maximum:
        maximum = num

print('msximum number is :',maximum)
