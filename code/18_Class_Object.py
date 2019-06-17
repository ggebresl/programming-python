'''
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
'''

class Animal:
    def behave(self):
        print('Jump')
        
class Cat(Animal):
    def action(self):
        print('in cat class')

obj = Cat()
obj.action()
obj.behave()

#wrappers or compositions

class vehicles(object):
    x=10
    y=20
    def __init__(self,color,name,cost):
        self.color = color
        self.name = name
        self.cost = cost
    def display(self):
        print('car color={}\ncar name={}\ncar cost={}\n'.format(self.color,self.name,self.cost))
car1 = vehicles('red','Fer',60000)
car2 = vehicles('blue','Jump',10000)
car1.display()
car2.display()


#type of variable
#1. Instance variable (Non static)
#2. Static variable(Class level variable)
#3. Local varable

#type of Methods
#1. Instance Method
#2. static method
#3. class method
