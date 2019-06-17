#li = [1,2,3,4,5,6,7,8,9]
'''
for i in li:
    print(i)
    
for i in range(10):
    print(i)
'''

def nextno(x):
    if x>0:
        yield x-1

for i in nextno(10):
    print(i)
    