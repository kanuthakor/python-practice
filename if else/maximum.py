x = int(input('enter number1 '))
y = int(input('enter number2 '))
z = int(input('enter number3 '))

if x > y:
    if x > z:
        max = x
    else:
        max = z
else:
    if (y > z):
        max = y
    else:
        max = z

print(max)

