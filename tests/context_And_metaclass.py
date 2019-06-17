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

# list --> []

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
print(d)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        