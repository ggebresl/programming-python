'''
scope of a variable
'''
'''
x=5
def outer():
    x=10
    print(x)
    def inner():
        x=15
        print(x)
    inner()

outer()
print(x)
'''
#1. What if i want to use global var in inner func
#2. What if i want to use Enclosing var in inner func
#global
'''
x=5
def outer():
    x=10
    print(x)
    def inner():
        global x
        x=20
        print(x)
        def innermost():
            x=30
            print(x)
        innermost()
    inner()

outer()
print(x)
'''
'''
x=5
def outer():
    x=10
    print(x)
    def inner():
        x=20
        print(x)
        def innermost():
            nonlocal x
            x=30
            print(x)
        innermost()
    inner()

outer()
print(x)
'''
'''
x=5
def outer():
    x=10
    print(x)
    def inner():
        global x
        print(x)
        def innermost():
            nonlocal x
            x=30
            print(x)
        innermost()
    inner()

outer()
print(x)
'''
'''
x=5
def outer():
    nonlocal x
    x=10
    print(x)
'''









