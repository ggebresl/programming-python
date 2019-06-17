'''
#OOP
#class, object, reference variable(object),
#how to create obj and invoke them,
#self, constructor (__init__),cls
#types of variables (instance variable)
#types of methods
#Inheritance
#wrapping Instead of Inheritance
'''
'''
class <classname>:
    ---attributes---
    ---methods---
'''
'''
class Students:
    #class variable
    bag = 1
    books = 5
    uniform = 2
    shoes = 2
    
    def myfunc(self):
        name='Sakeeb'
        print(name)
        print(self.pen,self.laptop,self.bag,self.books)
    
stud1 = Students()
stud2 = Students()

#dunder methods / Magic methods
print(Students.__dict__)
#instance variable
stud1.pen = 2
stud2.pen = 1
stud1.laptop = 1
stud1.books = 10

stud1.myfunc()

print('Bags=',stud1.bag,
      'Books=',stud1.books,
      'Uniforms=',stud1.uniform,
      'Shoe Pairs=',stud1.shoes)
print('Bags=',stud2.bag,
      'Books=',stud2.books,
      'Uniforms=',stud2.uniform,
      'Shoe Pairs=',stud2.shoes)

print(stud1.pen)
print(stud2.pen)

'''

''' 
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
obj.classfunc2()  

obj.classfunc()

Students.statmethod()  


Students.Bag = 1
stud1 = Students()
stud2 = Students()

stud1.uniform = 2
stud1.func()
stud3 = stud1.classfunc()
stud1.classfunc2()

stud3.x = 10
stud3.y = 20
stud3.res =  stud3.x+stud3.y
print(stud3.uniform)

print('stud1 = ',stud1.uniform)
print('stud2 = ',stud2.uniform)

'''


'''
#type of variable
#1. Instance variable (Non static)
#2. Static variable(Class level variable)
#3. Local varable

#type of Methods
#1. Instance Method (self)
#2. static method (no arguments)
#3. class method (cls)

'''

###Day2
'''
Create Employee Class
Add 5 Employees
eno, ename, esal
print the details of 5 employees
EmpNO = 100, EmpName = sakeeb, EmpSal = 10000 
'''

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

emp3.eno =  101
emp3.ename = 'Ann'


emp1.display()
emp2.display()
emp3.display()

'''

'''
class Employees:
    increment = 0.10
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        print('Employee is created')
    
    def display(self):
        print('EmpNO =',self.eno,'EmpName =',self.ename,'EmpSal =',self.esal)
        
    def updatesal(self):
        self.esal = self.esal + (self.esal*self.increment)
    
    def updatepercent(self):
        self.increment = eval(input('Please Enter Increment Value'))
    
emp1 = Employees(100,'sakeeb',100000)
emp2 = Employees(101,'Michael',20000)
emp3 = Employees(103,'Jeremy',30000)

emp1.display()
emp2.display()
emp3.display()

emp1.updatepercent()

emp1.updatesal()
emp2.updatesal()

emp1.display()
emp2.display()
emp3.display()

'''




'''
emp1.eno = 100
emp1.ename = 'sakeeb'
emp1.sal = 10000

emp2.eno = 101
emp2.ename = 'Michael'
emp2.sal = 20000

emp3.eno = 102
emp3.ename = 'Ann'
emp3.sal = 30000

emp4.eno = 103
emp4.ename = 'Jeremy'
emp4.sal = 40000

emp5.eno = 104
emp5.ename = 'Gary'
emp5.sal = 50000

emp1.display()
emp2.display()
emp3.display()
emp4.display()
emp5.display()
'''

#Inheritance
'''
class Parent:
    House = 'Manson'
    money = 200000000
    def display(self):
        print(self.House,self.money)
        
class Child(Parent):
    pass

obj = Child()
obj.display()
#print(obj.House,obj.money)
'''


class Parent:
    House = 'Manson'
    money = 200000000
    
    def display(self):
        print(self.House,self.money)
        
    def givehouse(self):
        print(self.House)
        
class child:
    def display(self):
        Parent().givehouse()
     
obj = child()

obj.display()



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
'''
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

'''
