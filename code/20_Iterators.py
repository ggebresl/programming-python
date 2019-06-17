#Iterators
#__iter__ and __next__

'''
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
'''
'''
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

'''

'''
for i in obj:
    print(i)
'''




''' 
  
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
'''
'''
itr_obj = iter(MyIterator('hello'))
  
print(next(itr_obj))
print(next(itr_obj))
print(next(itr_obj))
'''
'''
iter_obj = MyIterator(1,20)
for i in iter_obj:
    print(i)
'''    

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




































    
    
    
    
    
    
