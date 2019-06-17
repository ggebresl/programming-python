'''
--functions and type of arguments, scope of a variable
    First class Citizen
--Anonymeous Functions
    lambda, map, filter, reduce
'''

'''
def add():
    a = eval(input('enter first number'))
    b = eval(input('Enter Second Number'))
    c=a+b
    print(c)

add()
'''
'''
1. nested functions
2. function as an argument to another function
3. function returns another function
4. passing collections to function
5. closure function
'''

'''
def add(x,y):
    c=x+y
    print(c)

a = eval(input('enter first number'))
b = eval(input('Enter Second Number'))

add(a) #==>NO
add(a,b) #==> Yes
add(a,b,c) #== NO
'''

#Types of Arguments
'''
1. Positional argument
2. keyword argument / Default Argument
3. Variable Length Argument
4. Keyword Variable Length Argument
'''

#1. Positional
'''
def add(x,y):
    c=x+y
    print(c)
    
#add(10,20)
#add(10)
add(10,20,30)
'''

#2. Keyword / Default
'''
def add(x=5,y=7):
    c=x+y
    print(c)

#add()   
#add(10)
#add(10,20)
#add(10,20,30)
'''
'''
def add(x=5,y):
    c=x+y
    print(c)
#non-default argument follows default argument
#add()   
#add(10)
#add(10,20)
#add(10,20,30)
'''
'''
def add(x,y=5):
    c=x+y
    print(c)
    
#add()   
#add(10)
#add(10,20)
#add(10,20,30)
'''
'''
def add(empno=10,name='NONAME'):
    print(empno, name)
#add() #10 NONAME
#add('Sakeeb')
#add(name='Sakeeb')
#add('Sakeeb')
#add(100,'Sakeeb',10000.000) #Not Possible
'''   

#3. Variable Length Argument (tuple)
'''
def add(*var):
    #print(sum(var))
    for val in var:
        print(val**2)
add(10)
add(10,20)    
add(10,20,30)
add(10,20,30,40)
'''

#4. Keyword Variable Length argument (dictionary)
'''
def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)

#myfunc(a=10,b=20,c=30)
#myfunc(a,b=20,c=30) #not Possible
#myfunc(10,20,30,b=20,c=30) 
'''

'''
1. nested functions
2. function as an argument to another function
3. function returns another function
4. passing collections to function
5. closure function
'''

#function as an argument to another function
'''
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def main(func):
    a = eval(input('enter first number'))
    b = eval(input('Enter Second Number'))
    res = func(a,b)
    print(res)
    
main(div)
'''

#Nested Function
'''
def outer():
    def inner():
        print('Hello I am INNER')
        def innermost():
            print('Hello I am INNERMOST')
        innermost()
    inner()
    print('Hello I am OUTER')

outer()
'''

#returning function from another function
'''
def outer():
    print('Hello i am OUTER')
    def inner():
        print('Hello I am INNER')
    return inner

inner =  outer()
inner()
inner()
inner()
inner()
'''

#Closure Function
'''
def outer(x):#parent function
    def inner(): #child function
        print(x)
    return inner
inner =  outer(3000)
inner()
inner()
inner()
inner()
'''
'''
def parent(string):
    def child():
        str1 = string()
        return str1.upper()
    return child

def printfunc():
    return 'Hello SSSSSS'


#print(printfunc())

child = parent(printfunc)

print(child())
'''







































    

   






