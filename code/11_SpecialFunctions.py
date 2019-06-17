'''
--Special functions
    eval, zip, enumerate
'''

#1. eval()
'''
a = eval(input('enter a number'))
b = eval(input('enter second number'))
c = a+b
print(c)
'''

#[100,'sakeeeb',10000.00030]
'''
str1 = "100 sakeeeb 10000.00030"
print(str1.split())
'''
'''
str1 = "100 'sakeeeb' 10000.00030"
res = [eval(val) for val in str1.split()]
print(res)
'''

#2. zip()
itemno = [1,2,3,4,5]
itemname = ['item-1','item-2','item-3','item-4','item-5']
#expected outcome
#[(1,'item-1'),(2,'item-2'),(3,'item-3'),(),()]
'''
for t in zip(itemno,itemname):
    print(t)
'''  
'''  
res = [t for t in zip(itemno,itemname)]
print(res)
'''  
''' 
res = [t for t in zip(range(1,6),itemname)]
print(res)
'''
#3. enumerate()

res = {'USS'+str(k):v for k,v in enumerate(itemname)}
print(res)

'''
for k,v in enumerate(itemname):
    print(k,v)
'''
{'USS0': 'sakeeb', 'USS1': 'item-2', 'USS2': 'item-3', 'USS3': 'item-4', 'USS4': 'item-5'}



