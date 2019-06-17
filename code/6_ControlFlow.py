'''
Flow control
1. Conditional statement if,if-else, if-elif-else
2. Loop structures while, for
3. break and continue
4. pass
'''
'''
a = 10
if a!=10:
    print('YES')
else:
    print('NO')
'''
'''
num = int(input('Enter a no '))
if(num%2==0):
    print('EVEN')
else:
    print('ODD')
'''   
'''
num1 = int(input('Enter a no '))
num2 = int(input('Enter a no '))
if(num1>num2):
    print('Num1 is greater')
elif(num2>num1):
    print('Num2 is greater')
else:
    print('both are equal')
'''

'''
s = 'sakeeb'
if 'e' in s:
    print('yes it is there')
else:
    print("no it's not there")
'''

##loops
#1.while()
i=0
while(i<10):
    print(i)
    i+=1
else:
    print('Executed the code in while successfully')
'''
for ivar in iterable_oj:
    statement using ivar
'''
it = range(10) 
for i in it:
    print(i)
else:
    print('hello')

# break and continue
'''    
for i in range(10):
    if i==6:
        #break
        continue
    else:
        print(i)
    print('always executed')
'''

i=0
while(i<10):
    if i==6:
        break
    print(i)
    i+=1
else:
    print('Executed Successfully')










 
