'''
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
 '''
 
'''
f = open('inp.txt','w')
f.write('This is the content i want to write')
f.close()

f1 = open('inp.txt','r')
print(f1.read())
f1.close()
'''



'''
with open('inp.txt','w') as f:
    f.write('This is the content i want to write')
    
with open('inp.txt','r') as f:
    print(f.read())
'''   
'''
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
    statement = #'''
        #This is first line
        #this is second line
    #'''
    #fobj.write(statement)
'''
with ReadWriteFile('inp.txt','r') as fobj:
    print(fobj.read())

'''


#Creating CM using contextlib module
'''
1. Logging()
2. __enter__() ---> return val
3. with block
4. __exit__()
'''
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

'''















   