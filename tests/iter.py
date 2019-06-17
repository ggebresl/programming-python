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



























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        