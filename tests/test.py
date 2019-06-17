# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:53:42 2019

@author: ggebr
"""

class Students:
    #class variables
    bag = 1
    books = 5
    uniform = 2
    shoes = 2
    def myfunc(self):
        name = 'Sakeeb' # local variable
        print(name)
        print(self.pen, self.laptop, self.bag, self.books)
    
    
stud1 = Students() # Instance varible -  create an object from the class
stud2 =  Students()
#dunder methods/magic metods
print(Students.__dict__)
#instance variabble
stud1.pen = 3  #Automatially create a pen attribute
stud2.pen = 5
stud1.laptop = 1
stud1.books = 10
#stud1 is a reference variable
stud1.myfunc()

print('Bags= ', stud1.bag, 
      'Books= ',stud1.books,
      'Unifroms= ',stud1.uniform,
      'Shoe Pairs= ',stud1.shoes)

print('Bags= ', stud2.bag, 
      'Books= ',stud2.books,
      'Unifroms= ',stud2.uniform,
      'Shoe Pairs= ',stud2.shoes)




class Point:
    class_label_attribute = "call it at class label"
    '''Class attributes are shared across all instance of a class. 
       As all  human instances have 2 ears and 2 eyes  '''
       
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
    def __add__(self, other):
        return Point(self.x + other.x,  self.y + other.y)
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
        
        
p = Point(1, 2)
another = Point(1, 2)
print(p == another)
print( p + another)

p1 = Point(2, 4)
another1 = Point(1, 2)
print(p1 > another1)

p2 = Point(1, 2)
another2 = Point(2, 4)
print(p2 < another2)

print(str(p))



print(Point.class_label_attribute)
print(another.class_label_attribute)
Point.class_label_attribute = "changed values by another"

print(another.class_label_attribute)
print(Point.class_label_attribute)
 p.draw()
 
 class Employe:
    def __init__(self,eno , ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal   
        
    def fullname(self):
        print('{} {} {}'.format(self.eno, self.ename, self.esal))
    
emp1 = Employe('1' , 'Gary Gebreslassie', 90000)
emp2 = Employe('2', 'Ann', 609955)
emp3 = Employe('3', 'Nolawi', 60000)

print(emp1.fullname())
print(emp2.fullname())
print(emp3.fullname())

   '''
     
class Employee2:
    def __init__(self, , last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'  + last + '@company.com'
        
    def fullname(self):
        print('{} {}'.format(self.first, self.last))
        
        

emp1 = Employee('Gerawork' , 'Gebreslassie', 60000)
emp2 = Employee('Abeba', 'Gebre Meskel', 609955)
emp3 = Employee('Nolawi', 'Gerawork', None)
''''
'''
print(emp1.fullname())
print(Employee.fullname(emp1))

print(emp2.fullname())
print(Employee.fullname(emp2))

print('{} {}'.format(emp1.first, emp1.last))

print('{} {}'.format(emp2.first, emp2.last))


print(emp1)
print(emp2)

 


class Employe:
    def __init__(self,eno , ename, esal):
        self.
        self.last = last
        self.pay = pay
        self.email = first + '.'  + last + '@company.com'
        
    def fullname(self):
        print('{} {}'.format(self.first, self.last))
        


import csv
with open('C:\\2019\\python\\Classes\\apt.csv', 'r', newline='') as myCsvFile: 
    reader = csv.DictReader(myCsvFile)
    for row in reader.reader()
        print(row['column_name_1'], row['column_name_2'], row['column_name_3'], row['column_name_3'],
                      row['column_name_4'], row['column_name_5'])
                
'''

'''
print(isinstance(p, Point))
from pathlib import Path
Path(r"C:\2019\python\March\Homework") #WindowsPath('C:/2019/python/March/Homework')
Path()

Path() / "Homework/" #--.WindowsPath('Homework')

p = Path(r"C:\2019\python\March\Homework")
print(p)
print(p.home)
print(p.absolute)
print(p.name)

print(p.stem)
print(p.parent)
 
print(p.iterdir())

for ph in p.iterdir():
    print(ph)
    
paths = [py for py in p.glob(".py")]
print(paths)

############
'''

class Employees:
    increment = 0.10
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal
    
    def display(self):
        print('EMPNO = ', self.eno, 'EmpName = ', self.ename, 'EmpSal = ', self.esal)
        
    def updatesal(self):
        self.esal = self.esal + (self.esal * self.increment)
        
emp1 = Employees(100,'Sakeeb', 100000)
emp2 = Employees(101, 'Machael', 100000)
emp3 = Employees(1002, 'Jeremy', 100000)

emp1.display()
emp2.display()
emp3.display()
        
#03/14/2019
  
class Students:
     books = 5 #static or class level variable
    # pencil = 50
    #instnce method
     def func(self):
         Students.shoes = 2
         Students.uniform = 1
         
     #class Method
     @classmethod
     def calssfunc(cls):
        print("cls.books-->" + str(cls.books))
        return cls()
     @classmethod
     
     def calssfunc2(cls):
        cls.pencil = 50
        print("cls.pencil-->" + str(cls.pencil))
        return cls()
      
     #staticmethod
     @staticmethod
     def statmethod(): #for static methods arguments are not enforced
        number1 = 30 # local variables
        number2 = 40 
        return number1 + number2
  
Students.calssfunc2()


obj = Students()
obj.uniform = 10   # we are creating  an attribute called uniform on for this specif object object


#call static method on obj
result = obj.statmethod() # using instance variaable
result2 = Students.statmethod()  # using Class Name
# how to call class Method
obj3 = obj.calssfunc2 #ttributeError: type object 'Students' has no attribute 'uniform'
print(type(obj3))
obj3.pencil = 4

#study magic methods
#1
class NoLenSupport:

    
obj = NoLenSupport()
len(obj) #-->TypeError: object of type 'NoLenSupport' has no len()

class LenSupport:
    def __len__(self):
        return 66

 obj = LenSupport()
 len(obj)


from functools import total_ordering
class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []
        
        def __repr__(self):
            return 'Account({!r}, {!r})'.format(self.owner, self.amount)

        def __str__(self):
            return 'Account of {} with starting amount: {}'.format(self.owner, self.amount)


acc = Account('bob')  # default amount = 0
acc = Account('bob', 10)
print("name = ", acc.owner, ",amount = ",  acc.amount)


acc1 = Account('bob')
acc2 = Account('bob', 10)

repr(acc1)
print("acc.__repr__()" + repr(acc1))
print(str(acc))

repr(acc1)
print(str(Account))

str(acc1)

#2 Object Representation: __str__, __repr__

class Parent:
    House = "Mansion"
    money = 30000000
    
    def display(self):
        print(self.House, self.money)
        
    def givehouse(self):
        print(self.House)
        
        
class Child(Parent):
    def display():
        print("Child Display is running")
        #super().givehouse()
parObj = Parent()
parObj.display()     
parObj.givehouse()

obj = Child()
obj.display()

print(obj.House, obj.money)
#--------------------------------------------------
a = [1,2,3,4,5,6,7,8,9]
b = a.copy()
print(id(a))
print(id(b))
print(b)
#-------Iterator---------------------
# just- myitrObj = iter(li), next(myitrObj)
try:
    li = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    myitrObj = iter(li)
    print(next(myitrObj))
    print(next(myitrObj))
    print(next(myitrObj))
    print(next(myitrObj))
    print(next(myitrObj))
    print(next(myitrObj))
    print(next(myitrObj))
    print(next(myitrObj))
    print(next(myitrObj))  
except StopIteration:
    pass

try:
     li = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
     myiterobj = iter(li)
     count = 0
     while count < 10:
         print(next(myiterobj))
         count +=1
except StopIteration:
     pass   
 

class Iterator:
    def __init__(self, val):
        print('__init__ excecuted')
        self.val = val
        
    def __iter__(self):
        print('__iter__ executed')
        return Iterator(self)
    
    def __next__(self):
        print("__next__ exectued")
obj = Iterator('hello')
itr_obj = iter(obj)
next(itr_obj)


class Iterator:
    def __init__(self, val):
        self.val = val
        
    def __iter__(self):
        print('__iter__ executed')
        #return Iterator(self)
        return self
    
    def __next__(self, cnt):
        if self.val == self.cnt:
            raise StopIteration
            
        self.val == self.val + 1
    return self.val

count = 0      
obj = Iterator('hello')

for i in obj:
    if count > 10:
        break
    else:
        print("value of i = " + i)
        count += 1

#itr_obj = iter(obj)
#next(itr_obj)
























