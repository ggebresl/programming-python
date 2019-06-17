##datatype
#6. range(start,end,step)
#form-1
'''
a = range(10)
print(type(a))
print(a)
for i in a:
    print(i)
'''
#form-2
'''
a = range(4,11)
print(type(a))
print(a)
for i in a:
    print(i)
'''
#form-3
'''
a = range(1,11,2)
print(type(a))
print(a)
for i in a:
    print(i)
'''
#not allowed
'''
a = range(1.0,10.0)
'''

#7. list --> []
'''
a = [1,2,2,2,5,6,6,8,9,10]
print(type(a))
print(a)
'''
#features
'''
1. mutable
2. allows duplicate values
3. allows heterogeneous data
4. growable
5. maintains order of insertion
6. created by using []
7. list()
'''
'''
empli = [100, 'sakeeb', 10000.00]
print(empli)

print(empli[-1])
#print(empli[2])

empli[2] = 20000.00
print(empli)

empli.append('India')
print(empli)

empli.insert(3,'M')
print(empli)

empli.append('married')
print(empli)

empli.remove('married')
print(empli)

empli[2]=30000.00
print(empli)
'''
'''
a = [1,2,2,2,5,6,6,8,9,10]
print(a.count(2))
print(a.copy)

a.extend(b)
a.sort()
'''

#tuple ()
#features
#1. immutable
'''
t = (10,20,30,40)
print(type(t))
print(t)

t1 = 10,20,30,40
print(type(t))
print(t)
'''

#dictionary {key:value}
#features
'''
1.mutable object
2.key:value
3.keys are not allowed to be repeated and are immutable
4.values can be repeated
5.heterogeneous object
'''
'''
dic = {100:'Jeremy',101:'Gary',102:'Ann',103:'Michael'}
print(dic)
#adding new element
dic[104] = 'Steve'
print(dic)
#updating an element
dic[104] = 'John'
print(dic)
#delete and element
del dic[104]
print(dic)
dic[104]
'''

#packing and unpacking
'''
#packing
t = 10,20,30
#unpaking
a,b,c = t
'''

'''
dic = {100:'Jeremy',101:'Gary',102:'Ann',103:'Michael'}

for k,v in dic.items():
    print('key',k,'value',v)
'''

#dic = {100:'Jeremy',101:'Gary',102:'Ann',103:'Michael'}
#dic = {100:['Jeremy',12345678],101:['Gary',12345678],
#       102:['Ann',12345678],103:['Michael',12345678]}

#print(dic[100])
#print(dic[104])
#print(dic.get(100,'**Sorry employee not present**'))
#print(dic.get(104,'**Sorry employee not present**'))
#print(dic.popitem())

##set {} 
#features
#1. No duplicates values are allowed.
#2. Mutable object
#3. Order of insertion is not maintained
#4. Represented Using {}
#5. Does not support indexing
#6. Does not allow slicing.
#7. Heterogeneous object
#8. Growable
#9. set()
'''
s = {10,20,30,40,40,30,'sakeeb'}
print(type(s))
print(s)
s.add('ann')
s.add('gary')
print(s)
s.remove('sakeeb')
print(s)
'''

##Frozenset similar to set
#--> frozenset()
#--> immutable object
'''
l = [10,20,30,30,'sakeeb']
print(l)
fs = frozenset(l)
print(type(fs))
print(fs)
'''

##bytes
#--> immutable object
#--> 0 - 256
#--> bytes()
'''
x = [10,20,30,40]
b = bytes(x)
print(type(b))
print(b)
'''

##bytearray
#--> mutable object
#--> 0 - 256
#--> bytearray()
'''
x = [10,20,30,40]
b = bytearray(x)
print(type(b))
print(b[0])
b[0] = 100
print(b[0])
'''
##None
'''
n = None
print(type(n))
print(n)
'''
























