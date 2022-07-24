Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list
<class 'list'>
>>> list
<class 'list'>
>>> li =[23,34,54,23,34]
>>> li
[23, 34, 54, 23, 34]
>>> print('this is list')
this is list
>>> print('now set')
now set
>>> s={23,334,345,432,12,23}
>>> s
{12, 334, 432, 23, 345}
>>> type(s)
<class 'set'>
>>> type(li)
<class 'list'>
>>> print("set does not repeat the values andare always wreiten un {} ")
set does not repeat the values andare always wreiten un {} 
>>> print('now tuple')
now tuple
>>> t=(34,54,34,54,32,5465z)
SyntaxError: invalid syntax
>>> t=(34,23,54,23,34)
>>> type(t)
<class 'tuple'>
>>> str='kanuthakor'
>>> str
'kanuthakor'
>>> type(str)
<class 'str'>
>>> character = 'a'
>>> type(character)
<class 'str'>
>>> a=4
>>> type(a)
<class 'int'>
>>> range(10)
range(0, 10)
>>> 
>>> range
<class 'range'>
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,100,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> type(range(10))
<class 'range'>
>>> dictionary
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dictionary
NameError: name 'dictionary' is not defined
>>> d = {'kanu': 'dell', 'prashat': 'hp'}
>>> d.kanu
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d.kanu
AttributeError: 'dict' object has no attribute 'kanu'
>>> d.keys
<built-in method keys of dict object at 0x0000028E9F8BE700>
>>> d
{'kanu': 'dell', 'prashat': 'hp'}
>>> d.key
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d.key
AttributeError: 'dict' object has no attribute 'key'
>>> d.keys
<built-in method keys of dict object at 0x0000028E9F8BE700>
>>> d
{'kanu': 'dell', 'prashat': 'hp'}
>>> d.keys()
dict_keys(['kanu', 'prashat'])
>>> d.values()
dict_values(['dell', 'hp'])
>>> d['kanu']
'dell'
>>> g.get('prashat')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    g.get('prashat')
NameError: name 'g' is not defined
>>> d.get('dell')
>>> d
{'kanu': 'dell', 'prashat': 'hp'}
>>> d.get('kanu')
'dell'
>>> 