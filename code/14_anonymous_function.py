# lambda, map(), filter(), reduce()

#1. lambda
# where you small function
# only one expression
'''
def add(x,y):
    return x+y
'''
# lambda <args>:<expression>
'''
mul = lambda x,y:x+y if(x<y) else x-y
print(mul(20,10))
'''
#map(func_obj,itr1,itr2,itr3,...)
l1 = [1,2,3,4,5,6,7,8,9]
'''
def sqr(x):
    return x**2

res = []
for i in l1:
    res.append(sqr(i))
'''
res = map(lambda x:x**2,l1)
print(type(res))
print(list(res))


