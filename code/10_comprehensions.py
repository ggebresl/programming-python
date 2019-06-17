'''
--comprehensions
    list,dictionary,set
'''

li = [1,2,3,4,5,6,7,8,9]

#without using list comprehensions
'''
res = []
for n in li:
    if n%2==0:
        res.append(n**2)
    else:
        res.append(n)
print(res)
'''

#shorthand for writing if conditions
#(execute if true) if(condition) else (execute if flse)

#using list comprehensions
'''
res = [n**2 if n%2==0 else n for n in li]
print(type(res))
print(res)
'''
#Set comprehensions
'''
res = {n**2 if n%2==0 else n for n in li}
print(type(res))
print(res)
'''
#Dictionary Comprehensions
'''
res = {n:n**2 for n in li if n%2==0}
print(type(res))
print(res)
'''

















