Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 12 & 13
12
>>> ~12
-13
>>> 12 | 13
13
>>> 12 ^ 13
1
>>> 12 << 2
48
>>> 
>>> 48 >> 2
12
>>> import math
>>> x = math.sqrt(25)
>>> 
>>> x
5.0
>>> x = math.sqrt(15)
>>> x
3.872983346207417
>>> print(math.floor(2.9))
2
>>> print(math.ceil(2.1))
3
>>> import math
>>> 
================================ RESTART: Shell ================================
>>> from math import sqrt, pow
>>> sqrt(25)
5.0
>>> pow(3,2)
9.0
>>> 
================================ RESTART: Shell ================================
>>> import math as m
>>> math.sqrt(25)

>>> m.sqrt(25)
5.0
>>> math.sqrt(25)

>>> m.sqrt(25)
5.0
>>> 