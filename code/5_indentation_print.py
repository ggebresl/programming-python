#indentation

#print()
print('Hello World!')

#methods
#1. %
#2. commas (,)
#3. .format()
'''
a = int(input('Enter first no.'))
b = int(input('Enter Second no.'))
'''
#Addition of the no 10 and 20 is =  30
#print(a,b,a+b)
'''
c = a+b
print("Addition of the no %d and %d is =  %d"%(a,b,c))
'''
'''
%d - int
%f - float
%s - str, list , tuple, dic, ... 
'''
'''
sal =  1000.30303030303
print(sal)
#John has salary 1000.30
print("John has salary %.2f"%sal)
'''

#Method-2
'''
a = int(input('Enter first no.'))
b = int(input('Enter Second no.'))
print("Addition of the no",a,"and",b,"is =",a+b)
'''

#Method-3
#format()
#a = int(input('Enter first no.'))
#b = int(input('Enter Second no.'))
a = 10
b = 20
c = a+b
d = 60
print("Addition of the no a = {} and b = {} is = {}".format(b,a,c,d))

print("Addition of the no a = {1} and b = {0} is = {2}".format(b,a,c,d))

    
    
