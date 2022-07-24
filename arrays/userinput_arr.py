
from array import *

arr = array('i',[])

n = int(input('enter the length of the array : '))


for i in range(n):
    print('enter number',i+1,' ',end='')
    x = int(input())
    arr.append(x)


for i in arr:
    print(i)

print(arr)


val = int(input('enter the element you want to search : '))

# searching for an element in the array

k=0
for e in arr:
    if e == val:
        print('present at index',k)
        break
    k+=1

else:
    print('not found')

# searching using function

print('using functions index is ', arr.index(val))
