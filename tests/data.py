
ls = ["A", "Apple", "bonana"]
ls.append('grape') --> ['A', 'Apple', 'bonana', 'grape']

ls.clear()  ---> []


>>> c = ls.copy()
>>> ls
['A', 'Apple', 'bonana', 'grape']
>>> c
['A', 'Apple', 'bonana', 'grape']
>>>

>>> id(c)
10592664
>>> id(ls)
10593424
>>> 

>>> ls.count('A')
1


>>> ls.index('A')
0
