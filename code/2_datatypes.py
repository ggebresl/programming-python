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

dic = {100:'Jeremy',101:'Gary',102:'Ann',103:'Michael'}

for k,v in dic.items():
    print('key',k,'value',v)





























