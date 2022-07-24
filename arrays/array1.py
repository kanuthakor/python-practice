
import array        # we can also write like import arrays as a
                    # or can also written as from array import *

values = array.array('i', [5,9,8,5,25])

print(values)

print('address and type ')
print(values.buffer_info())     #prints address and type

values.reverse()    #reverses the array

print('reversed array is : ')
for i in range(5):          #printing content of arrays using for loop
    print(values[i])

print('using the length function')

for i in range(len(values)):
    print(values[i])


# or

print('another way')
for i in values:
    print(i)

print('copying arrays')

newarray = array.array(values.typecode, (a for a in values))

for e in newarray:          # can also be done using while
    print(e)
    
