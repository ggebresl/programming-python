# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:16:09 2019

@author: ggebr
"""
#1.  map 
#Compare the corresponding lists and write select the big number

li1 = [1, 2, 3, 4,5, 6, 7, 8, 9]
li2 = [7, 4, 9, 5, 6, 2, 3, 10,33]  

#res = [7, 4, 9, 5,6,6,7,10,33]


def compare(x, y):
    if x > y: 
        return x
    else:
        return y

'''
res = map(compare, li1, li2)
list(res)
''''


res = map(lambda x, y: x if (x >y) else y, li1, li2)
list(res)

#2 filter - filer out you do not want

def filt(x):
    if x %2 == 0:
        return True
    else:
        return False
    
 
res1 = []
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in li:
    if filt(i):
        res1.append(i)
print(res1)
    
print(list(filter(filt, li)))

#3. Reduce - returns a singe value
'''
functools.reduce
Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty.
'''
import functools
#  syntax: reduce(function-obj, iterable_obj) -->functools.reduce

li3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def addall(x, y):
    return x + y

res2 = functools.reduce(addall, li3)

print(res2)

res3 = functools.reduce(lambda x, y : (x + y), li3)
print(res3)
    

import sys

f = open('C:\\2019\\python\\inp.txt', 'r')

#data = f.read()

data = f.readlines()

for line in data:
    print(line.split("\n))
    
print(data.split("\n"))
f.close()

#14_anonymous_function
    
 # add x + y
 
add = (lambda x, y : x + y)
add(2, 4)

#sqr(x)

sqr = (lambda x : x**2)
sqr(7)

#map(func_obj,itr1,itr2,itr3,...)
l1 = [1,2,3,4,5,6,7,8,9]

 print(list(map(lambda x : x**2, l1)))


#13_scopeofVariable
 
#1. --> 10, 15, 5
 x=5
def outer():
    x=10
    print(x)
    def inner():
        x=15
        print(x)
    inner()

outer()
print(x)

#1. What if i want to use global var in inner func
#-->10, 20, 30,20
x=5
def outer():
    x=10
    print(x)
    def inner():
        global x
        x=20
        print(x)
        def innermost():
            x=30
            print(x)
        innermost()
    inner()

outer()
print(x)

#2. What if i want to use Enclosing var in inner func
#output"-->10, 20, 30, 5
x=5
def outer():
    x=10
    print(x)
    def inner():
        x=20
        print(x)
        def innermost():
            nonlocal x
            x=30
            print(x)
        innermost()
    inner()

outer()
print(x)

##output:-->no binding for nonlocal 'x' found
x=5
def outer():
    x=10
    print(x)
    def inner():
        global x
        print(x)
        def innermost():
            nonlocal x
            x=30
            print(x)
        innermost()
    inner()

outer()
print(x)
# error SyntaxError: no binding for nonlocal 'x' found
x=5
def outer():
    nonlocal x
    x=10
    print(x)
    
#12_Functions

def add():
    a = eval(input('enter first number'))
    b = eval(input('Enter Second Number'))
    c=a+b
    print(c)
print(add(c))
add()

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)


myfunc(a=10,b=20,c=30)

myfunc(a,b=20,c=30) #not Possible

myfunc(10,20,30,b=20,c=30) 

myfunc(10,20,30) 

t1 = (1, 2, 3, 4, 5, 6)
d1 = {'1': 1, '2': 2, '3': 3}

myfunc(t1)  

myfunc(d1)
#12_Functions
myfunc(t1, d1)    
#a an outer function returns only the top function if it has more thatn one function that returns a value  
 def outer():
    print('Hello i am OUTER')
    def innermost():
        print('Hello I am inner2')
    return innermost

    def inner():
        print('Hello I am INNER')
    return inner

innermost  = outer()

innermost()
inner =  outer()
inner()
inner2()

#12_Functions- eval, zip, enumerate

str1 = "100 'sakeeeb' 10000.00030"
res = [eval(val) for val in str1.split()]
print(res) #--> [100, 'sakeeeb', 10000.0003]

res = [val for val in str1.split()]
#zip

itemno = [1,2,3,4,5]
itemname = ['item-1','item-2','item-3','item-4','item-5']

for t in zip(itemno,itemname):
    print(t)
    
'''
(1, 'item-1')
(2, 'item-2')
(3, 'item-3')
(4, 'item-4')
(5, 'item-5')
'''

res = [t for t in zip(itemno,itemname)]
print(res)

'''
(1, 'item-1'), (2, 'item-2'), (3, 'item-3'), (4, 'item-4'), (5, 'item-5')]
'''
#3. enumerate()

res = {'USS'+str(k):v for k,v in enumerate(itemname)}
print(res)

for k,v in enumerate(itemname):
    print(k,v)

#10_comprehensions
    
#without using list comprehensions

li = [1,2,3,4,5,6,7,8,9]

res = []
for n in li:
    if n%2==0:
        res.append(n**2)
    else:
        res.append(n)
print(res)

res1 = [n**2 if n % 2 ==0 else n for n in li]
print(res1)

#Set comprehensions
res = {n**2 if n%2==0 else n for n in li}
print(type(res))
print(res)

#dectionary comprehensions

res = {n: n**2 if n%2==0 else n for n in li}
print(type(res))
print(res)

#9_String
s = 'B2A1D3C4'

s1=s2=output=''
for i in s:
    if i.isalpha():
        s1=s1+i
    else:
        s2=s2+i
print(''.join(sorted(s1))+''.join(sorted(s2)))
#OR
print(''.join(sorted(s1)+sorted(s2)))

s = 'a4b3'

output=''
for i in s:
    if i.isalpha():
        output=output+i #-->ab
        previous = i  #-> ab
    else:
        output=output+previous*(int(i)-1) #->aaaaabbb

print(output)

 
#Input1 :- SAKEEB
#Input2 :- SHEIKH
#Output :- SSAHKEEIEKBH
s1=input('Enter a First String')
s2=input('Enter a Second String')

s1 = 'SAKEEB'
s2= 'SHEIKH'

output=''
i=j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]  
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
    
print(output)
#9_str

s3 = "12AB45"
i = 0
output=''
output2 =''
for i in s3:
    if i.isdecimal():
        output=output+i  
        
    else:
        output2= output2 + i

print(output)
print(output2)

s = 'sakeeb'
print(s.count('e'))
print(s.index('a'))

str1 = """playing played    plays moving 


jumping eating matching"""

list_str = str1.split()
print(list_str)


s = 'jamesbond007'
print(s.isalnum())

s1 = '123'
print(s.isalnum())

s = 'sakeeb'
print(s.isalpha()) 

s = '12'
print(s.isalpha()) 


#join

s = 'SAKEEB'
li = list(s)
print(li)

#8_string

s = 'B2A1D3C4'
alp = []
num = []

for ch in s:
    if ch.isalpha():
        alp.append(ch)  #-- ['B', 'A', 'D', 'C']
    else:
        num.append(ch)  #-- ['2', '1', '3', '4']

alp.sort()
num.sort()
print(alp)
print(num)
alp.extend(num)


s1=s2=final=''

for ch in s:
    if ch.isalpha():
        s1+=ch
    else:
        s2+=ch
output = ''.join(sorted(s1)+sorted(s2))
print(output)

#7_questions
#Question-1 Print the below statement by replacing dashed area with the respective input accepted from user (using input())
'''--name-- is --age-- years old learning --lang name--- programming language lives in ---city-- city
'''
name = input('name ')
age = eval(input("age "))
lang_name = input("lang name ")
city = input("city ")
print("{} is {} years old learning {} programming language lives in {}".format(name, age, lang_name, city))

# default(implicit) order
#default_order = "{}, {} and {}".format('John','Bill','Sean')






















