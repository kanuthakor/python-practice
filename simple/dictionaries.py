Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data ={1:kanuthakor, 2:prashant,4:lakkho}
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    data ={1:kanuthakor, 2:prashant,4:lakkho}
NameError: name 'kanuthakor' is not defined
>>> data = {1:'kanuthakor', 2:'prashant',4:'lakkho'}
>>> data
{1: 'kanuthakor', 2: 'prashant', 4: 'lakkho'}
>>> data ={1:kanuthakor, 2:prashant, 4:lakkho}
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data ={1:kanuthakor, 2:prashant, 4:lakkho}
NameError: name 'kanuthakor' is not defined
>>> data
{1: 'kanuthakor', 2: 'prashant', 4: 'lakkho'}
>>> data[3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data[3]
KeyError: 3
>>> data [1]
'kanuthakor'
>>> data.get(1)
'kanuthakor'
>>> data.get(3)
>>> print(data.get(3))
None
>>> DATA
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    DATA
NameError: name 'DATA' is not defined
>>> data.get(1,'not mentioned')
'kanuthakor'
>>> data.get(3,'not found')
'not found'
>>> keys = ['kanu','prashant','parth']
>>> values=['python','chemistry','dhammal']
>>> new data = dict(zip(keys,values))
SyntaxError: invalid syntax
>>> data = dict(zip(keys,values))
>>> new = dict(zip(keys,values))
>>> data
{'kanu': 'python', 'prashant': 'chemistry', 'parth': 'dhammal'}
>>> new
{'kanu': 'python', 'prashant': 'chemistry', 'parth': 'dhammal'}
>>> neew['kanu']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    neew['kanu']
NameError: name 'neew' is not defined
>>> new['kanu']
'python'
>>> new['hitu'] = 'laptop'
>>> new
{'kanu': 'python', 'prashant': 'chemistry', 'parth': 'dhammal', 'hitu': 'laptop'}
>>> del new['hitu']
>>> new
{'kanu': 'python', 'prashant': 'chemistry', 'parth': 'dhammal'}
>>> program = { 'js':'atom', 'cs':'vs', 'python': ['python','sublime'],'java':{'jse': 'netbeans','jee', 'eclipse'}}
SyntaxError: invalid syntax
>>> program = { 'js':'atom', 'cs':'vs', 'python': ['python','sublime'],'java':{'jse': 'netbeans','jee': 'eclipse'}}
>>> program['js]
	
SyntaxError: EOL while scanning string literal
>>> program['js']
'atom'
>>> program['python']
['python', 'sublime']
>>> program['python'][1]
'sublime'
>>> program['java']
{'jse': 'netbeans', 'jee': 'eclipse'}
>>> ['java']['jee']
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    ['java']['jee']
TypeError: list indices must be integers or slices, not str
>>> program['java']['jee']
'eclipse'
>>> 