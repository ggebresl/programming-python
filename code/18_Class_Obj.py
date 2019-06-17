#1. OOP
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

'''
class Employee:
    def __init__(self,x,y):
        self.x = x #instance variables
        self.y = y
    def input(self,x,y): #instance method
        self.x = x
        self.y = y
    def display(self):
        print(self.x,self.y)

obj = Employee(10,20)
'''
#obj.__display()

#method Vs Constructor
'''
1. any name         ---- __init__
2. when called
   then only executes---  when obj is created
3. per obj. can be ---  only once
    executed any no. of
    times

4. used to write ----   to declare instance
    business logic      variables

'''

'''
class Employee:
    def __init__(self,eno,ename):
        self.eno = eno
        self.ename = ename

    def display(self):
        print(self.eno)
        print(self.ename)

e1 = Employee(100, 'Sakeeb')
e2 = Employee(101, 'Paul')
e1.display()
e2.display()
'''
#types of variables
#1. Instance Variable (Non-Static)
#2. Static Variable (Class-Level Variables)
#3. Local Variable

#1> Instance Variable (Non-Static)
#--> varies from obj to obj
#--> Seperate copy will be created for every obj.
#--> Declared inside constructor using self
#--> inside class -- using self keyword
#--> outside class -- reference variable

#how to get the variable in objectreference

#t1 t2 t3
#x
#Where we can declare instance variable?
#1. inside constructor.
#2. inside instance method.
#3. Outside class by using reference variable.

#2> Static Variable (Class-level variable)
'''
class MyClass:
    a=10  #Static variable
    def __init__(self,x):
        self.x=x
        MyClass.var = 200
    def display(self):
        print(self.x)
        print(MyClass.var)

obj1 = MyClass(100)
print(MyClass.__dict__)
'''
#Where we can declare Static variable?
#1. with the class directly
#2. inside Constructor Using Classname
#    eg: MyClass.c = 20
#3. inside the instance method
#4. inside classmethod by using
#   cls variable or classname
'''
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
print(obj.__dict__)
print(MyClass.__dict__)
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
#obj1.m1()
#print(obj.__dict__)
#print(MyClass.__dict__)
obj1.x=200

print(obj1.x,' ',obj2.x)
print(MyClass.a)
'''
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
'''
class MyClass:
    def stat_func():
        print('inside static method')

obj = MyClass()
'''

#Inheritance
'''
class Animal:
    def behave(self):
        print('this can Jump')

class Cat(Animal):
    def act(self):
        print('this is cat class')

obj = Cat()
obj.behave()
obj.act()
'''

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
        return Animal.behave()

obj = Cat()






















