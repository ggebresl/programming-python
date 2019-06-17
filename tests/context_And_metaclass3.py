# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:00:34 2019

@author: ggebr
"""


emp1 = [100,'Sakeeb', 100000]
emp2 = [101, 'Machael', 200000]
emp3 = [1002, 'Jeremy', 300000]

emp_li = [emp1, emp2, emp3]

'''
lisEmp.append(emp1)
lisEmp.append(emp2)
lisEmp.append(emp3)
'''


class IterEmpl:
    def __init__(self, empli):
        self.empli = empli
        self.cnt = 0
    def __iter__(self):
        return self
    def __next__(self):
        retVal = self.empli[self.cnt]
        self.cnt += 1
        return retVal

iterObj = IterEmpl(emp_li)

    for i in iterObj:
        try:
            print(i)
        
        except IndexError:
            break
        
        

# Let us move on to generators
# The object that remembers the last value is called  a generator
# To generate numbers on the fly, then the oject should remebers the last generated value
#That oject which remembers the last generated value is called  a generator
            
        
for i in range(10):
    print(i)
        

def nextno(x):
    return x + 1
print(nextno(10))


def mygen(n):
    li = []
    for i in range(n):
        li.append(i)
    return li

for j in mygen(10):
    print(j)
    
# This is good for generators exmple 
    
def mygen2(n):

    for i in range(n):
       print('n =' + str(n))
       print('i = ' + str(i))
       yield i
      
for j in mygen2(10):
    print('j = ' + str(j))
 
''''
def nextno4(x):
    if x > 0:
        yield x -1 
        
for i in nextno2(10):
    print(i)
        
  '''''      
  
def gensquare(n):
      for i in range(n):
          if i % 2 == 0:
              yield i*i
              
for j in gensquare(10):
    print(j)
        
#coroutines
def match(pattern):
        print('Looking for ' + pattern)
        try:
            while True:
                s = (yield)
                if pattern in s:
                    print(s)
        except GeneratorExit:
            print("=== Done ===")
''' We initialize it with a pattern, and call __next__() 
    to start execution:'''

m = match("Jabberwock")
m.__next__()
''' The call to __next__() causes the body of the function to be 
     executed, so the line "Looking for jabberwock" gets printed out.
     Execution continues until the statement line = (yield) is 
     encountered. 
'''
m.send("the Jabberwock with eyes of flame")
m.send("came whiffling through the tulgey wood")
m.send("and burbled as it came")
m.send("Gerawork Jabberwock")
m.close()

''' Then, execution pauses, and waits for a value to be sent to m.
    We can send values to it using send.
'''


###################################################
def read(text, next_coroutine):
        for line in text.split():
            next_coroutine.send(line)
        next_coroutine.close()

text = 'Commending spending is offending to people pending lending!'
matcher = match('ending')
matcher.__next__()  #-->Looking for ending
read(text, matcher)

'''' 
We can break up match into a filter and a consumer. The filter 
would be a coroutine that only sends on strings that match its
 pattern
'''
def match_filter(pattern, next_coroutine):
        print('Looking for ' + pattern)
        try:
            while True:
                s = (yield)
                if pattern in s:
                    next_coroutine.send(s)
        except GeneratorExit:
            next_coroutine.close()
'''
And the consumer would be a function that printed out lines 
sent to it.
'''
def print_consumer():
        print('Preparing to print')
        try:
            while True:
                line = (yield)
                print(line)
        except GeneratorExit:
            print("=== Done ===")
'''
When a filter or consumer is constructed, 
its __next__ method must be invoked to start its execution.
'''
printer = print_consumer()
printer.__next__()  #--.Preparing to print

matcher = match_filter('pend', printer)
matcher.__next__()  #-->Looking for pend
read(text, matcher)

################################################           

def Consumer():
    while True: 
        val = (yield) #the key yield stops the whle loop. It stops for the send() function. The generator functions, uses yield to return values
        #With this syntax, execution pauses at this statement
        # until the object's send method is invoked with an argument
        print(val**3) # To exectue this function we have
        
# A function that always runs in the back-ground. To execute this in the background we have at least to call it once
consume = Consumer()
#When a fileter or consumer is constructed, its __next__() method must be invoked to start execution
consume.__next__()
consume.send(5) 
#Then, execution resumes,with 'value' being assigned to the value of data
############################################################## 
# let us see a conumer and producer functions below:       
#Consumer     
def Consumer1():
    try:
        while True: 
             #print('Consumer1() started')
             val = (yield)
             print(val**3)
    except GeneratorExit:
        print("===closed Coroutine===")
        
# Producer function
def Producer1(n, coroutine):
    for i in range(n):
        coroutine.send(i)
    coroutine.close()
        
consume1 = Consumer1()  
consume1.__next__()
Producer1(10,consume1)
'''
you can also use the next function
consume1.send(10)
consume1.close()
'''

########################################
# Now let us see how filter is implimented using Consumer and Producdr
#Filter recives data from producer and pass data to the consumer  

def Consumer2():
    try:
        while True:
            print('Consumer2() started')
            val,val2 = (yield)
            print(val2, val**3)
    except GeneratorExit:
        print("===closed Coroutine===")
# Producer function
def Producer2(n, coroutine):
    for i in range(n):
        a = i+1
        coroutine.send((i,a))
        
    coroutine.close()
       
consume2 = Consumer2()  
consume2.__next__()
Producer2(10,consume2)

############ Now let us user filter#########################

#Filter recives data from producer and pass data to the consumer
#The following shows all 3: Consumer, Filter, and Producer3  

def Consumer3():
    try:
        while True:
            #print('Consumer2() started')
            val = (yield)
            print(val, ',', val**3)
            
    except GeneratorExit:
        print("===Consumer3 closed Coroutine===")
        
def Filter():
    try:
        while True:
            val, coroutine = (yield)
            if val%2==0:
               coroutine.send(val)
               #print(val)
    except GeneratorExit:
        print("===Filer closed Coroutine===")
                
# Producer function
def Producer3(n, coroutine,consume3):
    for i in range(n):   
        coroutine.send((i,consume3))
        #print(val)
        
    coroutine.close()
       
consume3 = Consumer3()  
filt = Filter()
consume3.__next__()
filt.__next__()

Producer3(10,filt,consume3)

###################################################################

def Consume4(statement):
    try:
        while True:
            print('waiting for an input pattern from send')
            pattern = (yield)
            for word in statement.split():
                 if word.endswith(pattern):
                     print(word)
    except:
        print("===Closed Coroutine===")
stamt =  '''consumer producer comming going running playing finding discussing jumping entertainer '''
cor1 = Consume4(stamt)
cor1.__next__()
cor1.send('ing')
print('-----words that end with er----------')
cor1.send('er')

### you can make the above code generic by:

def Consume5(pattern):
    try:
        while True:
            statement = (yield)
            for word in statement.split():
                 if word.endswith(pattern):
                     print(word)
    except:
        print("===Closed Coroutine===")
        
statement =  '''consumer producer comming going running playing finding discussing jumping entertainer '''

cor_for_ing = Consume5('ing')
cor_for_er = Consume5('er')

cor_for_ing.__next__()
cor_for_er.__next__()

cor_for_ing.send(statement)
cor_for_er.send(statement)              

cor_for_ing.close()
cor_for_er.close()

##to see the list of variables in a dir()

for var in dir():
    if not var.startswith('_'):
        print(var)
        del(var)

###Contxt Mangement and metadataclasses
class TestContextMgr:
    def __enter__(self):
        print('Started Using Resource')
        return 100
    def __exit__(self,exc_type, exc_val, exc_tb): #exc_type:exception type, exception value, exception trace back
        print("Resource Released")
        if exc_type == None:
            print('No Exception Generate')
        else:
            print(exc_type, exc_val, exc_tb)
            
with TestContextMgr() as var:
    print('I am inside with block')
    print(var)
    
##demonstrate contextmgr with files as well
#C:\2019\python\Classes
    
with open('inp1.txt', 'w') as f:
    f.write("This is the content I want to write")
    
with open('inp1.txt', 'r') as f:
    print(f.read())
##########################
    
# write your out contxt magarer for files read/write
    
class ReadWriteFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        print('Opening File to read/read')
        self.f = open(self.filename, self.mode)
        return self.f
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        print('File closed successfully')
    
with ReadWriteFile('inp1.txt', 'r') as fobj:
    print(fobj.read())

with ReadWriteFile('inp1.txt', 'a') as fobj:
    statment = 'GAry- This is the data that is being written by fobj.write'
    fobj.write(statment)

##########################3
    
#Creating Context Manager using contextlib module
    

'''
There is a process we have to follow in the followig order
1. Logging() - must be called 1st
2. __enter__()  --> return val
3. with block - gets exectued
4. __exit__()
please read more about this contextlib
'''
import contextlib

@contextlib.contextmanager
def Logging():
    print('code for enter() method before yield')  
    # the code before yield is enter()
    yield 'Inside the with block'
    #the code after yield is exit() 
    print("code for exit() method after yield")
        
with Logging() as l:
    print(l)
    
    for i in dir():
        if not i.startswith('_'):
            print(i)
            
##########The next topic is about metaclasses 
# 1. type(int) --> type . So type is in built metaclass which is responsible of creating everythin
# class creates object. type creates class

def ClassFactory(cname):
    if cname == 'Foo':
        class Foo:
         address = '5 Thayer Circle Wakefield, MA'  
         def getFullName(self, fn, ln):
                self.firstName = fn
                self.lastName = ln
                return  "Full Name --> " + fn + " " + ln
        return Foo
    
    else:
        class Bar:
            a = 10
            b= 20
        return Bar
    
cname = 'Foo'
Myclass = ClassFactory(cname)
print(Myclass)
print(Myclass.getFullName(Myclass, 'Gerawor', 'Gebreslassie'))
'''
print(type(Myclass))
<class 'type'>
'''
obj = Myclass()
print(obj.__dict__)
print(obj)
print(obj.getFullName('Abeba', 'Gile ') + obj.address)

cname1 = 'Bar'
Myclass = ClassFactory(cname1)
obj2 =  Myclass()
print(Myclass.__dict__)
    
##how to make it more dynamic and control the behavior of the class
## type is a metaclass by default

MyClass1 = type('Foo1', (), {'var1':'100', 'var2':'200'})
#That means you can dynmically call the above class and create a brand new class
print(MyClass1)
obj_1 = MyClass1()
print(obj_1.var1, obj_1.var2)

####let us control the behavior of the class you will create

class UpperAttrMetaclass(type) : 
    #def __init__(self):
        #after this new object is created
        #print("This is Constructor")
    
    #please note when  a class is creted, this automatically gets executed
    
    def __new__(cls, cname, bases, dic):
        print("This is  __new__")
        upperattr = {} # dict to hold values from incoming dic, but in upper case
        
        for name, val in dic.items():
            if not name.startswith('__'):
                upperattr[name.upper()]= val
            else:
                upperattr[name]=val
        # return the metaclass. When you creat a class dynmically you call new method of this metaclass (cls?) 
        return type.__new__(cls, cname, bases, upperattr)
    
class MyMetaClass(metaclass=UpperAttrMetaclass):
    firstName = 'gerawork'
    lastname = 'gebreslassie'
    def myFunc():
        print("This myFunc")
        
##study all the classes from day one 
# 1. basics
        
s = '''hello how are you'''
#s[start:end:step]
print(s)
print(s[0:5])
print(s[:5])
print(s[6:17])
print(s[6:])
print(s[::2])
print(s[::3])
print(s[6:-1])
print(s[::-1])
#s[start:end:step]

#Rerverse
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 30]
print(num[::-1])
#output:[30, 20, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#--------------------------------------------------------------    
#2. datatypes

a = range(10)
print(type(a))
print(a)

for i in a:
    print(i)   
        

a = range(4,11)
print(type(a))
print(a)
for i in a:
    print(i)

a = range(1,11,2)
print(type(a))
print(a)
for i in a:
    print(i)

#--------------------------------------------------------------
# 3. list --> []


a = [1,2,2,2,5,6,6,8,9,10]
print(type(a)) #--><class 'list'>
print(a)

#features of list
'''
1. mutable
2. allows duplicate values
3. allows heterogeneous data
4. growable
5. maintains order of insertion
6. created by using []
7. list()
'''
empli = [100, 'sakeeb', 10000.00]
print(empli) #==>[100, 'sakeeb', 10000.0]

print(empli[-1])
print(empli[-2])
print(empli[2])
#Modify
empli[2] = 20000.00
print(empli)  #-->[100, 'sakeeb', 20000.0]    

empli.append('India')
print(empli) #-->[100, 'sakeeb', 20000.0, 'India']

empli.insert(3,'M')
print(empli) #-->[100, 'sakeeb', 20000.0, 'M', 'India']

empli.append('married')
print(empli) #-->[100, 'sakeeb', 20000.0, 'M', 'India', 'married']

empli.remove('married')
print(empli) #-->[100, 'sakeeb', 20000.0, 'M', 'India']

a = [1,2,2,2,5,6,6,8,9,10]
 
b = a.copy()
print(id(a), id(b))

a.extend(b) 
print(a) #-->#-->[1, 2, 2, 2, 5, 6, 6, 8, 9, 10, 1, 2, 2, 2, 5, 6, 6, 8, 9, 10]
print(b) #-->[1, 2, 2, 2, 5, 6, 6, 8, 9, 10]

a.sort() # This sorts modify a
print(a)  #-->1, 1, 2, 2, 2, 2, 2, 2, 5, 5, 6, 6, 6, 6, 8, 8, 9, 9, 10, 10]

c = b.copy()
print(c)
d = c.extend(b)      
print(d) #-->None
print(c) #-->[1, 2, 2, 2, 5, 6, 6, 8, 9, 10, 1, 2, 2, 2, 5, 6, 6, 8, 9, 10]
d = c.sort()
print(c) #-->[1, 1, 2, 2, 2, 2, 2, 2, 5, 5, 6, 6, 6, 6, 8, 8, 9, 9, 10, 10]
print(d) #--> None

#--------------------------------------------------------------
#4. tuple ()

#features
#1. immutable

t = (10,20,30,40)
print(type(t)) #--><class 'tuple'>
print(t)  #-->(10, 20, 30, 40)

t1 = 10,20,30,40
print(type(t))
print(t) #-->10, 20, 30, 40)

#packing and unpacking 

#packing
t = 10,20,30
print(t) #-->(10, 20, 30)
print(type(t)) #--><class 'tuple'>


#unpaking
a,b,c = t #--> a,b,c = t
print(a,b,c) #-->10 20 30

#--------------------------------------------------------------
#5. dictionary {key:value}
#features

'''
1.mutable object
2.key:value
3.keys are not allowed to be repeated and are immutable
4.values can be repeated
5.heterogeneous object
'''
dic = {100:'Jeremy',101:'Gary',102:'Ann',103:'Michael'}
print(dic) #-->{100: 'Jeremy', 101: 'Gary', 102: 'Ann', 103: 'Michael'}

#adding new element
dic[104] = 'Steve'
print(dic) #-->{100: 'Jeremy', 101: 'Gary', 102: 'Ann', 103: 'Michael', 104: 'Steve'}

#updating an element
dic[104] = 'John'
print(dic) #-->{100: 'Jeremy', 101: 'Gary', 102: 'Ann', 103: 'Michael', 104: 'John'}

#delete and element
del dic[104]
print(dic) #-->{100: 'Jeremy', 101: 'Gary', 102: 'Ann', 103: 'Michael'}

dic[104] #-->KeyError: 104


dic1 = {100:'Jeremy',101:'Gary',102:'Ann',103:'Michael'}
print(dic1) #-->{100: 'Jeremy', 101: 'Gary', 102: 'Ann', 103: 'Michael'}


for k,v in dic1.items():    
    print('key',k,'value',v)
    

#--------------------------------------------------------------
#6. set {} 
#features
#1. No duplicates values are allowed.
#2. Mutable object
#3. Order of insertion is not maintained
#4. Represented Using {}
#5. Does not support indexing
#6. Does not allow slicing.
#7. Heterogeneous object
#8. Growable
#9. set()

s = {10,20,30,40,40,30,'sakeeb'}

print(type(s)) #--><class 'set'>
print(s) #-->{40, 10, 'sakeeb', 20, 30}

s.add('ann')
print(s) #-->{40, 10, 'sakeeb', 20, 'ann', 30}

s.add('gary')
print(s)  #-->{40, 10, 'gary', 'sakeeb', 20, 'ann', 30}

s.remove('sakeeb')
print(s) #-->{40, 10, 'gary', 20, 'ann', 30}
#--------------------------------------------------------------
#7. Frozenset similar to set
#--> frozenset()
#--> immutable object

l = [10,20,30,30,'sakeeb']

print(l) #-->[10, 20, 30, 30, 'sakeeb']

fs = frozenset(l)
print(type(fs)) #--><class 'frozenset'>

print(fs) #-->frozenset({10, 20, 'sakeeb', 30})



#--------------------------------------------------------------
#8 bytes
#--> immutable object
#--> 0 - 256
#--> bytes()

x = [10,20,30,40]
b = bytes(x)
print(type(b)) #--><class 'bytes'>
print(b) #-->

#--------------------------------------------------------------
# 9.--> bytearray()
#--> mutable object
#--> 0 - 256



x = [10,20,30,40]
b = bytearray(x)

print(type(b))  #--><class 'bytearray'>

print(b[0]) $-->10

b[0] = 100
print(b[0]) #-->100

#--------------------------------------------------------------
## 10. None

n = None
print(type(n)) #--><class 'NoneType'>
print(n) #None

#--------------------------------------------------------------
#3_Interactive_Help
#dir() and help()
#print(dir())

#print(dir(__builtins__))
#li = dir()
#print(li)
#print(help(pow))
#help('modules')
'''

import math
print(math.radians(180))
''''
#--------------------------------------------------------------
#indentation

a = int(input('Enter first no --> '))
b = int(input('Enter Second no-->'))
c = a+b
print("Addition of the no %d and %d is =  %d"%(a,b,c))

'''
%d - int
%f - float
%s - str, list , tuple, dic, ... 
'''

sal =  1000.30303030303
print(sal)
print("John has salary %.2f"%sal) #John has salary 1000.30

#Method-2

a = int(input('Enter first no.'))
b = int(input('Enter Second no.'))

print("Addition of the no",a,"and",b,"is =",a+b)

#Method-3
#format()

a = 10
b = 20
c = a+b
d = 60
print("Addition of the no a = {} and b = {} is = {}".format(b,a,c,d))

print("Addition of the no a = {1} and b = {0} is = {2}".format(b,a,c,d))

#6_ControlFlow

num = int(input('Enter a no '))
if(num%2==0):
    print('EVEN')
else:
    print('ODD')

#if,elif els
    
num1 = int(input('Enter a no '))
num2 = int(input('Enter a no '))
if(num1>num2):
    print('Num1 is greater')
elif(num2>num1):
    print('Num2 is greater')
else:
    print('both are equal')

# in operator
    
s = 'sakeeb'
if 'e' in s:
    print('yes it is there')
else:
    print("no it's not there")

#whie
i=0
while(i<10):
    print(i)
    i+=1
else:
    print('Executed the code in while successfully')
    
#for
it = range(10) 
for i in it:
    print(i)
else:
    print('hello')
#continue
    
for i in range(10):
    if i==6:
        #break
        continue
    else:
        print(i)
    print('always executed')

#break
i=0
while(i<10):
    if i==6:
        break
    print(i)
    i+=1
else:
    print('Executed Successfully')
    
    
########while##########
s1 = 'Gerawork'
s2= 'TesfaGiorgis' 
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

#change the above to for loop

1 = 'Gerawork'
s2= 'TesfaGiorgis' 
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

#string
    
s = 'B2A1D3C4'
alp = []
num = []

for ch in s:
    if ch.isalpha():
        alp.append(ch)
    else:
        num.append(ch)
print(alp) #==>  ['B', 'A', 'D', 'C'] holds only letters 
print(num) #==>  ['2', '1', '3', '4']

alp.sort()
num.sort()

print(alp) #==>   ['A', 'B', 'C', 'D']
print(num) #==>   ['1', '2', '3', '4']

alp.extend(num)
print(''.join(alp))


st = "Ghis1D 124A GC4 t2 a b1 1bbe 2be e1"
charHolder = []
numHolder = []
for ch in st:
    
    if ch.isalpha():   
        charHolder.append(ch)
    elif ch.isspace():
        pass
    else:
         numHolder.append(ch)
         
print(charHolder)
print(numHolder)

charHolder.sort()
numHolder.sort()

print(charHolder)
print(numHolder)
print(charHolder.count('b'))

charHolder.extend(num)
print(''.join(charHolder))
print(''.join(numHolder))
#####

s = 'B2A1D3C4'

s1=s2=final=''

for ch in s:
    if ch.isalpha():
        s1+=ch
    else:
        s2+=ch
output = ''.join(sorted(s1)+sorted(s2))
print(output)

############3
#sting methods
#1. len() function
string = 'sakeeb'
print(len(string ))
lis_t = [1,2,3,4,5,6,6,7,8,9]
print(len(lis_t)) #  --> 10. len is good for strings as well as lists

tup_l = (1,2, 3, 4, 4) 
print(len(tup_l))  #--> 5 good for tuple as well. 

se_t = {10,20,30,40,40,30,'sakeeb'}

print(len(se_t)) #--> 5 duplicate is not counted


dic = {100:'Jeremy',101:'Gary',102:'Ann',103:'Michael'}
print(len(dic)) #--> 4

# 2. count function
print(string.count('e'))
print(string.count('a'))
print(string.count('sak'))

#3. index()
s = 'sakeeb'
print(s.index('a')) #--> 1. Returns position
print(s.index('e')) #--> 3 

#3. startswith(), endswith()

str1 = "playing played plays moving jumping eating matching"
print(str1.startswith('play')) #-->True
print(str1.endswith('ing')) #==>True


#4.split()
str1 = '''playing played    plays 


moving jumping eating matching'''

list_str = str1.split()  # you can create lists using split from a string (str)
print(list_str) #-->['playing', 'played', 'plays', 'moving', 'jumping', 'eating', 'matching']

a = "Hello"
list_a = a.split()
print(list_a) #-->['Hello']

for word in list_str:
    if word.endswith('ing'):
        print(word)

for word in list_str:
    if word.startswith('play'):
        print(word)


s = "playing,played,plays,moving,jumping,eating,matching"
li = s.split(',')
print(li) #-->['playing', 'played', 'plays', 'moving', 'jumping', 'eating', 'matching']
#From above, you change strings to lists and then use list or []

def wordsPattern(list_str,pattern):  
    print("the pattern = "   + "'" + pattern + "'" )
    for word in list_str:
        if word.endswith(pattern):
            print(word)
     
wordsPattern(list_str, 'ing') 

#isalnum(), isalpha(), isdecimal()

s = 'jamesbond007'
print(s.isalnum()) #-->True

s = 'sakeeb'
print(s.isalpha())  #-->True

s = '12345'
print(s.isdecimal()) #True

#lower, upper, islower, isupper

s = 'sakeeb'
print(s.upper()) #SAKEEB

s = 'Sakeeb'
print(s.lower()) #sakeeb

s = 'Sakeeb'
print(s.islower()) #False

s = 'sakeeb'
print(s.islower()) #True

s = 'SAKEEB'
print(s.isupper()) #True

#join

s = 'SAKEEB'
li = list(s)
print(li)  #-->['S', 'A', 'K', 'E', 'E', 'B']. you can change string to list

print(','.join(li)) #-->S,A,K,E,E,B
print(''.join(li)) #--.SAKEEB

#chr() and ord()
print(chr(66))
print(ord('B'))

#######################
#10_comprehensions for list,dictionary,set

li = [1,2,3,4,5,6,7,8,9]

#without using list comprehensions
listComp = []
for n in li:
    if n%2 == 0:
        print(n)
    
listComp = [n for n in li if n%2 ==0]
print(listComp ) #-->[2, 4, 6, 8] horizatal output
######################

res = []
for n in li:
    if n%2 == 0:
        res.append(n**2)
    else:
        res.append(n)
print(res) #-->[1, 4, 3, 16, 5, 36, 7, 64, 9] --horizatal output
    
res = [ n**2 if n%2 == 0 else n for n in li]
print(type(res)) #--><class 'list'>
print(res ) #-->[1, 4, 3, 16, 5, 36, 7, 64, 9]

#Set comprehensions

res = { n**2 if n%2 == 0 else n for n in li}
print(type(res))  #--> <class 'set'>
print(res ) #-->{64, 1, 3, 4, 5, 36, 7, 9, 16}

#Dictionary Comprehensions

res = {n:n**2 if n%2 == 0 else n for n in li}

print(type(res))  #--> <class 'dict'>
print(res ) #-->{1: 1, 2: 4, 3: 3, 4: 16, 5: 5, 6: 36, 7: 7, 8: 64, 9: 9}


res = {n:n**2 for n in li if n%2==0}
print(type(res))
print(res)

#11_SpecialFunctions
'''eval, zip, enumerate'''
#1. eval() handles int, float, "45" +"45" -->4545, 4.5 + 7 = 11.5
a = eval(input('enter a number -->'))
b = eval(input('enter second number-->'))
c = a+b
print(c)

str1 = "100 sakeeeb 10000.00030" # change this str to a list format
print(str1.split())  #-->['100', "'sakeeeb'", '10000.00030']

str1 = "100 'sakeeeb' 10000.00030"
res = [eval(val) for val in str1.split()]
print(res)

#2. zip()

itemno = [1,2,3,4,5]
itemname = ['item-1','item-2','item-3','item-4','item-5']

#expected outcome
#[(1,'item-1'),(2,'item-2'),(3,'item-3'),(),()]


sezResult = zip(itemno, itemname)
for i in sezResult:
    print(i)

for t in zip(itemno,itemname):
    print(t)


res = [t for t in zip(itemno,itemname)]
print(res)

res = [t for t in zip(range(1,6),itemname)]
print(res)


#3. enumerate()

for enum in enumerate(itemname):
    print(enum) # see output below: add tuple indexing
'''  
(0, 'item-1')
(1, 'item-2')
(2, 'item-3')
(3, 'item-4')
(4, 'item-5')
'''
    
for k,v in enumerate(itemname):
    print(k,v)
    
res = {str(k):v for k,v in  enumerate(itemname)}
print(type(res)) #<class 'dict'>
print(res) #-->{'0': 'item-1', '1': 'item-2', '2': 'item-3', '3': 'item-4', '4': 'item-5'}


res = {'USS'+str(k):v for k,v in enumerate(itemname)}
print(res)

#12_Functions   
'''
--functions and type of arguments, scope of a variable
    First class Citizen
--Anonymeous Functions
    lambda, map, filter, reduce
'''      
        
def add():
    a = eval(input('enter first number'))
    b = eval(input('Enter Second Number'))
    c=a+b
    print(c)

add()

'''
1. nested functions
2. function as an argument to another function
3. function returns another function
4. passing collections to function
5. closure function
'''

#Types of Arguments

'''
1. Positional argument
2. keyword argument / Default Argument
3. Variable Length Argument
4. Keyword Variable Length Argument
'''

#1. Positional
def add(x,y):
    c=x+y
    return c

print(add(11, 6)) #17

print(add(x = 11, y = 6)) #-->17

#2. Keyword / Default
def add(x=5,y=7):
    c=x+y
    return c
add()
add(6)
add(6,6)
add(x=10, y=30) #by keyword



def add(x=5,y):
    c=x+y
    return c
#add() # SyntaxError: non-default argument follows default argument
add(10,10)

def add(x,y=5):
    c=x+y
    return c

add(10) #--> 15
add(34, 10)-->44

def add(empno=10,name='NONAME'):
    print(empno, name)
    
add() #-->10 NONAME
add(45,'Gera')#-->45 Gera
add('Sakeeb') #-->Sakeeb NONAME

#3. Variable Length Argument 

def add(*var):
    for val in var:
        print(val**2)

add(10)
add(10,20)    
add(10,20,30)
add(10,20,30,40)

def add(*var):
    print(sum(var),max(var),min(var))


add(10)
add(10,20)    
add(10,20,30)
add(10,20,30,40)

#4. Keyword Variable Length argument (dictionary)

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)

myfunc(a=10,b=20,c=30)
myfunc(10,20,30,b=20,c=30) 
#output is below:
'''
(10, 20, 30)
{'b': 20, 'c': 30}
'''

'''
1. nested functions
2. function as an argument to another function
3. function returns another function
4. passing collections to function
5. closure function
'''

#function as an argument to another function

#let us the following funcions
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


def main(func):
    print("funct Name ", func)
    a = eval(input('enter first number -->'))
    b = eval(input('Enter Second Number -->'))
    res = func(a,b)
    print(res)
    
main(add)
main(sub)
main(mul)
main(div)

#Nested Function

def outer():
    def inner():
        print('Hello I am INNER')
        def innermost():
            print('Hello I am INNERMOST')
        innermost()
    inner()
    print('Hello I am OUTER')

outer()

#returning function from another function

def outer():
    print('Hello i am OUTER')
    def inner():
        print('Hello I am INNER')
    return inner

inner =  outer()
inner()
inner()
#Factory - they remember  den or denminator
def make_is_divisible(den):
    def is_divisibile(num):
        print(num, den)
        return num % den == 0
    return is_divisibile

is_div_2 = make_is_divisible(2)
is_div_2(200)

result = make_is_divisible(2)(200)

#Closure Function

def outer(x):#parent function
   # print("from parnt x = " + str(x))
    def inner(): #child function
        print(x)
    return inner
inner =  outer(3000)
inner()
inner()
inner()
inner()


def parent(string):
    def child():
        str1 = string()
        return str1.upper()
    return child

def printfunc():
    return 'Hello SSSSSS'

child = parent(printfunc)
print(child())
#####################

#13_scopeofVariable
#scope of a variable

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

x=5
def outer():
    x=10
    print(x)
    def inner():
        global x
       # x=15
        print(x)
    inner()

outer()
print(x)

        
x=5
def outer():
    x=10
    print(x)
    def inner():
        global x
        x=20  # replaces the global value from x=5 to x=20
        print(x)
        def innermost():
            x=30
            print(x)
        innermost()
    inner()

outer()
print(x)
        
#2. What if i want to use Enclosing var in inner func

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
        
        
x=5
def outer():
    nonlocal x
    x=10
    print(x)
# 
def make(N):
    def action(x):
        return x**N  #the inner function remembers N (state)
    return action

f = make(2)
f(100)

g = make(3)

g(100)

#####################
#14_anonymous_function
 # lambda, map(), filter(), reduce()
   
#1. lambda
# where you have small function
# only one expression

def add(x,y):
    return x+y
add(199, 1)

# lambda <args>:<expression>
add = lambda x, y: x + y
    
print(add(45, 45))


addorSub = lambda x,y:x+y if(x<y) else x-y
print(addorSub (10,20))

#map(func_obj,itr1,itr2,itr3,...)


def sqr(x):
    return x**2
print(sqr(x))

sq = lambda x:x**2
print(sq(x))

#map(func_obj,itr1,itr2,itr3,...)

l1 = [1,2,3,4,5,6,7,8,9]

res = []
for i in l1:
    res.append(sqr(i))
print(res)

#map(func_obj,itr1,itr2,itr3,...) 
#The collection could be a list or a set  
res1 = map(lambda x:x**2,l1)
print(type(res1))
print(list(res1))


lis1 = [1,2,3,4,5,6,7,8,9]
res2 = map(sqr,lis1)
print(list(res2))

print(list(map(lambda x, y,z: x + y + z, [1,2,3], [4,5,7],[1,1.1])))


##############################################
#15_commandline
#sys module
import sys
print(sys.version)
print(sys.copyright)
print(sys.stderr.write('error msg'))
print(sys.stdout.write('this is stdout msg'))
print(sys.argv)
print(sys.argv[1:])
for i in sys.argv[1:]:
    print(i)
    
########
#6_FileOperations
'''
open(<filepath>,<filemode>)
Filemode - r, w, a, rb, wb
'''
#reading file

f = open('inp1.txt','r')
data = f.read()
print(data)
f.close()

#writing a file

f = open('inp.txt','a')
f.write('This is new content that i want to write')
f.close()

f = open('inp.txt','r')
data = f.readlines()
for line in data:
    print(line.split())
f.close()

#####################################
#17_Assignment
#18_CLASS_DAY1andDAY2

class Students:
    #class variable
    bag = 1
    books = 5 #static / class level
    uniform = 2
    shoes = 2
    
    def myfunc(self):
        name='Sakeeb'
        print(name)
        print(self.pen,self.laptop,self.bag,self.books)
    
'''
Before creating the object, type 'Students.__dict__ ' in the python interactive to see:
Students.__dict__
Out[743]: 
mappingproxy({'__module__': '__main__',
              'bag': 1,
              'books': 5,
              'uniform': 2,
              'shoes': 2,
              'myfunc': <function __main__.Students.myfunc(self)>,
              '__dict__': <attribute '__dict__' of 'Students' objects>,
              '__weakref__': <attribute '__weakref__' of 'Students' objects>,
              '__doc__': None})
'''
print(Students.__dict__)

stud1 = Students()
stud2 = Students()

#instance variable
stud1.pen = 20
stud1.laptop = 10
stud1.books = 100
print(stud1.__dict__) #-->{'pen': 20, 'laptop': 10, 'books': 100}
print(stud1.pen) #-->20

stud1.myfunc()
'''
Sakeeb
20 10 1 100
'''
stud2.pen = 1000
print(stud2.pen) #-->100

stud2.myfunc()
print(stud2.__dict__) #-->{'pen': 1000}


print('Bags=',stud1.bag,
      'Books=',stud1.books,
      'Uniforms=',stud1.uniform,
      'Shoe Pairs=',stud1.shoes)

print('Bags=',stud2.bag,
      'Books=',stud2.books,
      'Uniforms=',stud2.uniform,
      'Shoe Pairs=',stud2.shoes,
      'Pen =', stud2.pen)  # -->Bags= 1 Books= 5 Uniforms= 2 Shoe Pairs= 2 Pen = 1000


print(stud1.pen) #-->20
print(stud2.pen) #-->1000


###

class Students:
    books = 5 #static / class level
    
    #instance Method
    def func(self):
        Students.shoes=2
        Students.uniform = 1
   
    #Instancemethod    
    def classfunc2(self):
        print(self.uniform)
        
    #Class Method
    @classmethod
    def classfunc(cls):
        print(cls.uniform)
        return cls()
    
    #StaticMethod
    @staticmethod    
    def statmethod():
        x=10
        y=20
        c=x+y
        return c

      
obj = Students()    
Students.statmethod()  #-->30


Students.Bag = 1  #Students.__dict__ --> 'books': 5, 'Bag': 1
stud1 = Students()
stud2 = Students()

stud1.uniform = 2 #--> {'uniform': 2}

stud1.func()  # forces to execute the instance Method to perform at Stdents lable/class label
'''
'books': 5,
'Bag': 1,
'shoes': 2,
'uniform': 1})
'''

stud3 = stud1.classfunc()

stud1.classfunc2()

stud3.x = 10
stud3.y = 20
stud3.res =  stud3.x+stud3.y
print(stud3.uniform)

print('stud1 = ',stud1.uniform)
print('stud2 = ',stud2.uniform)

'''
#type of variable
#1. Instance variable (Non static)
#2. Static variable(Class level variable)
#3. Local varable

#type of Methods
#1. Instance Method (self)
#2. static method (no arguments)
#3. class method (cls)
#############################
'''

class Employees:
    company = 'USS'
    def display(self):
        print(self.eno,self.ename,self.esal,self.company)

emp1 = Employees()
emp2 = Employees()
emp3 = Employees()

emp1.eno =  100
emp1.ename = 'sakeeb'
emp1.esal = 100000

emp2.eno =  101
emp2.ename = 'Ann'
emp2.esal = 200000

emp3.eno =  102
emp3.ename = 'Micael'
emp3.esal = 500000

emp1.display() #-100 sakeeb 100000 USS
emp2.display() #101 Ann 200000 USS
emp3.display() #102 Micael 500000 USS

################
#Inheritance

class Parent:
    House = 'Manson'
    money = 200000000
    def display(self):
        print(self.House,self.money)
        
class Child(Parent):
    pass

obj = Child()
obj.display()

#########################
class Parent:
    House = 'Manson'
    money = 200000000
    
    def display(self):
        print(self.House,self.money)
        
    def givehouse(self):
        print(self.House)
        
class child:
    def display(self):
        Parent().givehouse()  # observe how this is called
     
obj = child()

obj.display()

#####

class Animal:
    def behave(self):
        print('this can Jump')

class Cat(Animal):
    def act(self):
        print('this is cat class')

obj = Cat()
obj.behave()
obj.act()

#wrapping instead of inheritance

class Animal:
    def behave(self):
        print('this can Jump')
    def acting(self):
        print('Do something')

class Cat(Animal):
    def act(self):
        print('this is cat class')
    def behave(self):
        #print(super().behave()) #or
        #print(Animal().behave()) # to override Aniaml do beow
        print("No Meyaw!")

obj = Cat()
obj.act()
obj.behave()


###18_Class_Obj
1. OOP
#class, object, reference variable,
#how to create obj and invoke them,
#self, constructor (__init__)
#types of variables (instance variable)
#types of methods
#Inheritance
#wrapping Instead of Inheritance

#2. Command line arguments
#3. import keyword
#4. Creating own modules
#5. pickling and unpickling
#6. sys module
#7. regular expression

class Employee:
    def __init__(self,x,y):
        self.x = x #instance variables
        self.y = y
        
    def input(self,x,y): #instance method
        self.x = x
        self.y = y
        
    def display(self):
        print(self.x,self.y)

obj = Employee(10,20) #-->10 20
obj.display()

#Where we can declare instance variable?
#1. inside constructor.
#2. inside instance method.
#3. Outside class by using reference variable.

#2> Static Variable (Class-level variable)

class MyClass:
    a=10  #Static variable
    def __init__(self,x):
        self.x=x
        MyClass.var = 200
        
    def display(self):
        print(self.x)
        print(MyClass.var)

obj1 = MyClass(100) # Remember we are passinng self, x (self, 100)

obj1.display()
#obj1.__dict__
#Output--> {'x': 100}

print(MyClass.__dict__)

'''
   print(MyClass.__dict__)
    {'__module__': '__main__', 'a': 10, '__init__': 
    <function MyClass.__init__ at 0x000002D1BF348B70>, 
    'display': <function MyClass.display at 0x000002D1BF348AE8>, 
    '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__':
        <attribute '__weakref__' of 'MyClass' objects>,
        '__doc__': None, 'var': 200}
        
'''

#Where we can declare Static variable?
#1. with the class directly
#2. inside Constructor Using Classname
#    eg: MyClass.c = 20
#3. inside the instance method
#4. inside classmethod by using
#   cls variable or classname

class MyClass:
    a=10  #Static variable
    def __init__(self,x):
        self.x=x
    def display(self):
        print(self.x)
    @classmethod #decorater
    def m1(cls):
        cls.f = 40
        cls.g = 50
        MyClass.h=60

obj = MyClass(10)
obj.m1()

print(MyClass.__dict__)
'''
appingproxy({'__module__': '__main__',
              'a': 10,
              '__init__': <function __main__.MyClass.__init__(self, x)>,
              'display': <function __main__.MyClass.display(self)>,
              'm1': <classmethod at 0x2d1bf36b048>,
              '__dict__': <attribute '__dict__' of 'MyClass' objects>,
              '__weakref__': <attribute '__weakref__' of 'MyClass' objects>,
              '__doc__': None,
              'f': 40,
              'g': 50,
              'h': 60})
'''

print(obj.__dict__) #-->{'x': 10}

print(MyClass.__dict__)

#################################

'''
#5. inside stacticmethod by using
#   cls variable or classname
'''

class MyClass:
    a=10  #Static variable
    
    def __init__(self,x):
        self.x=x
        
    def display(self):
        print(self.x)
        
    @staticmethod
    def m1():
        MyClass.ivar=100

obj1 = MyClass(10)
obj2 = MyClass(20)
obj1.m1()
print(obj.__dict__) #-->'x': 10}

obj1.x=200  
print(obj1.__dict__) #--> {'x': 200}

print(obj1.x,' ',obj2.x) #-->200   20

print(MyClass.a) #-->10


#######################
#6. Outside of class by using Classname

#1. Instance method
#2. static method
#3. class method

class MyClass:
    def inst_func(self):
        print('inside Instance method')
    
    @staticmethod
    def stat_func(x,y,z):
        print('inside static method')

    @classmethod
    def cls_func(cls):
        print('inside class method')

obj = MyClass()
obj.inst_func()
obj.stat_func(10,20,30)
obj.cls_func()

###################




#wrapping instead of inheritance

class Animal:
    def behave(self):
        print('this can Jump')
    def acting(self):
        print('Do something')

class Cat:
    def act(self):
        print('this is cat class')
        
    def behave(self):
        return Animal().behave()
     
obj = Cat()
obj.behave()
##################################
#18_Class_Object

class Calc:
    def __init__(self,x,y):
        print('constructor Executed')
        self.x = x
        self.y = y
        
    def add(self):
        print(self.x+self.y)
        
    def sub(self):
        print(self.x-self.y)
        
    def mul(self):
        print(self.x*self.y)
        
    def div(self):
        print(self.x/self.y)
        
obj = Calc(20,30)

print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())
##########################################

#19_ExceptionHandling
'''
ZeroDivisionError
NameError
TypeError
ValueError
'''
#try, except, finally, else

try:
    #a = int(input('enter a number'))
    #if a==10:
#        raise ValueError('The Number 10 is not allowed')
    
    #a = 0 #-->This is ZeroDivideError
    a = 11
    if a==10:
        raise ValueError
    b = 20
    #b = '20' #--> will generate TypeError
    c = b/a
    print(c)

except TypeError:
    print('This Is TypeError')
except ValueError:
    print('The Number 10 is not allowed')
except ZeroDivisionError:
    print('This is ZeroDivideError')
except NameError:
    print('This is NameError')
except SyntaxError:
    print("invalid syntax")
else:
    print('Code executed Successfully')
finally:
    print('This code always gets executed')


#####################################################################
#20_Iterators
    
    #Iterators
#__iter__ and __next__
    
#Build a tv remore control
'''
1. Create a refrence to the Iterator
    itr = RemoteControl()
2. Create an object of iter(itr)
    iterObj = iter(itr)
3 loop through the iterable object (iterObj) that was created in step 2
'''
class RemoteControl:
    def __init__(self):
        self.channels = ["HBO", "CNN", "BBC", "ABC", "ESPAN"]
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]
        
itr = RemoteControl()
iterObj = iter(itr)

for ir in iterObj:
    print(ir)

################################################################
    
li = [1,2,3,4,5,6,7,8,9]
for i in li:
    print(i)
        
try:
    li = [1,2,3,4,5,6,7,8,9]
    myiterobj = iter(li)
    while True:
        print(next(myiterobj)) 
except StopIteration:
    pass

+++++
class Iterator:
    def __init__(self,val,cnt):
        print('__init__ executed')
        self.val = val
        self.cnt = cnt
    
    def __iter__(self):
        #print('__iter__ executed')
        return self
    
    def __next__(self):
        #print('__next__ executed')
        if self.val==self.cnt:
            raise StopIteration
        self.val = self.val+1
        return self.val
    
    def display(self):
        print('hello')

obj = Iterator(0,10)
#iterobj = iter(obj)
#print(next(iterobj))

for val in obj:
    print(val)


#---------------------------
class MyIterator:
    def __init__(self,value,max_cnt):
        self.value = value-1
        self.max_cnt = max_cnt
        self.cnt = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.cnt>=self.max_cnt:
            raise StopIteration
        self.cnt = self.cnt+1
        self.value = self.value + 1
        return self.value

myIter = MyIterator(0,5)
myIterObj = iter(myIter)

for  mi in myIterObj:
    print(mi)
#-------------------
    
emp1 = [100,'sakeeb',10000]
emp2 = [101,'Gary',20000]
emp3 = [102,'Ann',30000]

emp_li = [emp1,emp2,emp3]

class IterEmp:
    def __init__(self,empli):
        self.cnt = 0
        self.empli = empli
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.cnt+=1
        empdet = self.empli[self.cnt-1]
        #self.cnt+=1
        return empdet
    
itrobj = IterEmp(emp_li)
for empdet in itrobj:
    try:
        print(empdet)
    except IndexError:
        break
    
#--------------------------------
#22_Generator

#li = [1,2,3,4,5,6,7,8,9]
'''
for i in li:
    print(i)
'''  
for i in range(10):
    print(i)



def nextno(x):
    if x>0:
        yield x-1


for i in nextno(10):
    print(i)
    
#-----------------------------
    #23_Coroutine
    
#Coroutines
GAry
#Consumer Function

def Consumer():
    try:
        while True:
            val= (yield)
            print(val,',',val**3)
    except GeneratorExit:
        print("===Consumer Closed Coroutine===")

def Filter():
    try:
        while True:
            val,coroutine = (yield)
            if val%2==0:
                coroutine.send(val)
                #print(val)
    except GeneratorExit:
        print("===Filter Closed Coroutine===")    
                
#Producer Function
def Produce(n,coroutine,consume):
    for i in range(n):
        coroutine.send((i,consume))
    
    coroutine.close()
        

consume = Consumer()
filt = Filter()
consume.__next__()
filt.__next__()

Produce(10,filt,consume)


#--------------------------------------------------------------------
def Consume(statement):
    try:
        while True:
            pattern = (yield)
            for word in statement.split():
                if word.endswith(pattern):
                    print(word)
    except:
        print("===Closed Coroutine===") 

    
stmt = '''consumer producer comming going running playing 
finding discussing, junping entertainer'''

cor1 = Consume(stmt)
cor1.__next__()

cor1.send('ing')
cor1.send('er')
cor1.close()




def Consume(pattern):
    try:
        while True:
            statement = (yield)
            for word in statement.split():
                if word.endswith(pattern):
                    print(word)
    except:
        print("===Closed Coroutine===") 



stmt = '''consumer producer comming going running playing 
finding discussing, junping entertainer'''


cor_for_ing = Consume('ing')
cor_for_er = Consume('er')
cor_for_ing.__next__()
cor_for_er.__next__()
cor_for_ing.close()
cor_for_er.close()

#-------------------------------------------------
#24_ContextManager


class TestManager:
    def __enter__(self):
        print('Started Using Resource')
        return 10
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('Resource Released')
        if exc_type == None:
            print('No Exception Generated')
        else:
            print(exc_type,exc_val,exc_tb)
        
        
with TestManager() as var:
        print('i am inside with block')
        print(var,x)

 

f = open('inp.txt','w')
f.write('This is the content i want to write')
f.close()

f1 = open('inp.txt','r')
print(f1.read())
f1.close()



with open('inp.txt','w') as f:
    f.write('This is the content i want to write')
    
with open('inp.txt','r') as f:
    print(f.read())
 

class ReadWriteFile:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        print('Opening File to Read/Write')
        self.f = open(self.filename,self.mode)
        return self.f
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.f.close()
        print('File Closed Successfully')

with ReadWriteFile('inp.txt','r') as fobj:
    print(fobj.read())
     
with ReadWriteFile('inp.txt','a') as fobj:
    statement = '''
        #This is first line
        #this is second line
    '''
    fobj.write(statement)

with ReadWriteFile('inp.txt','r') as fobj:
    print(fobj.read())




#Creating CM using contextlib module
'''
1. Logging()
2. __enter__() ---> return val
3. with block
4. __exit__()
'''

import contextlib

@contextlib.contextmanager
def Logging():
    print('Code for enter method before yield')
    #enter()
    yield 'Inside the with block'
    #exit()
    print('Code for exit method after yield')


with Logging() as l:
    print(l)
############################################################################
#strings - studt
    
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])


count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')
#------------------

str = 'cold'
list_enumerate = list(enumerate(str))

print('list(enumerate(str) = ', list_enumerate)
'''
Sometimes we may wish to ignore the escape sequences inside a string. 
To do this we can place r or R in front of the string. This will imply 
that it is a raw string and any escape sequence inside it will be ignored.
'''
print("This is \x61 \ngood example")
'''But look the next line'''
print(r"This is \x61 \ngood example")

print(R"This is \x61 \ngood example")

default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)


# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

def yell(text):
    print(text.upper())
yell('Hello')

bark = yell
bark('This is Gerawork')

print(bark.__name__)

list(map(yell, ['hello', 'hey', 'hi']))


def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

speak('Hello, World')

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper
print(get_speak_func(0.7))

speak_func = get_speak_func(0.7)
speak_func('Hello')

#---------------Gary------------------------------
'''
Take a good look at the inner functions whisper and yell now. 
Notice how they no longer have a text parameter? But somehow 
they can still access the text parameter defined in the parent
function. In fact, they seem to capture and “remember” the 
value of that argument.

Functions that do this are called lexical closures (or just closures, 
for short). A closure remembers the values from its enclosing 
lexical scope even when the program flow is no longer in that scope

'''
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

get_speak_func('Hello, World', 0.7)()

'''
In practical terms this means not only can functions return behaviors 
but they can also pre-configure those behaviors
Here’s another bare-bones example to illustrate this idea

In this example make_adder serves as a factory to create and 
configure “adder” functions. Notice how the “adder” functions 
can still access the n argument of the make_adder function 
(the enclosing scope).

'''

def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)

plus_5 = make_adder(5)

plus_3(4)

plus_5(4)
add(5, 3)

#Lamda expression
add = lambda x, y: x + y
add(5,3)


'''
Take a look at the following example and keep the words function 
expression in your head while you do that:
    
There’s another syntactic difference between lambdas and regular 
function definitions: Lambda functions are restricted to a single
expression. This means a lambda function can’t use statements or
annotations—not even a return statement.

How do you return values from lambdas then? Executing a lambda function 
evaluates its expression and then automatically returns its result. 
So there’s always an implicit return statement. That’s why some people
refer to lambdas as single expression functions.
'''  

(lambda x, y: x + y)(5, 3)

x = 20
y = 30

(lambda x, y: x + y)(x, y)

''''
Syntax :
[Expression for item in list if condition]
Example :  A = [x for x in list if x%2==0]
'''

#Iterator example

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)
    
class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value

repeater = Repeater('Hello')

for item in repeater:
    print(item)



repeater = Repeater('Hello')
iterator = repeater.__iter__()
while True:
    item = iterator.__next__()
    print(item)


#Let’s see what other Python iterators do to solve this problem. I’m going to construct a simple container, a list with a few elements, and then I’ll iterate over it until it runs out of elements to see what happens:

my_list = [1, 2, 3]

iterator = iter(my_list)

next(iterator)

#############

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

br = BoundedRepeater('Gera', 10)
itr = iter(br)
for i in itr:
    print(i)

#Coroutines with its GeneratorExit  exceptin 

def match(pattern):
        print('Looking for ' + pattern)
        try:
            while True:
                s = (yield)
                if pattern in s:
                    print(s)
        except GeneratorExit:
            print("=== Done ===")



 m = match('ing')
 m.__next__() # strat execution
 
 m.send('this is coming and going to the streets')
 m.send('Not sure')
 m.send('eating and drinking')
 m.close()

#Context manager
 class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()


files = []
for _ in range(10000):
    with File('foo.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)

#######################################################################
from contextlib import contextmanager
@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()

files = []
for x in range(100000):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)
    
for f in files:
    if not f.closed:
        print('not closed')





















