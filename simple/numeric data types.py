Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=4.444
>>> type(num)
<class 'float'>
>>> num =4 +4j
>>> type(num)
<class 'complex'>
>>> a=5
>>> type(a)
<class 'int'>
>>> b = float(a)
>>> type(b)
<class 'float'>
>>> b
5.0
>>> c = complex(a,b)
>>> c
(5+5j)
>>> type(c)
<class 'complex'>
>>> b<a
False
>>> b>a
False
>>> b==a
True
>>> bo = b==a
>>> bo
True
>>> type(bo)
<class 'bool'>
>>> int(bo)
1
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> int(True)
1
>>> int(Flase)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(Flase)
NameError: name 'Flase' is not defined
>>> int(False)
0
>>> inta =3
>>> inta
3
>>> int a =4
SyntaxError: invalid syntax
>>> 