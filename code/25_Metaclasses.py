'''
class MyClass:
    a = 10

obj = MyClass()


MyClass = type()
obj = MyClass()
'''
'''
def ClassFactory(Cname):
    if Cname == 'Foo':
        class Foo:
            x=10
            y=20
        return Foo
    else:
        class Bar:
            a=10
            b=20
        return Bar
        
cname = 'Bar'
MyClass = ClassFactory(cname)

print(MyClass)
obj = MyClass()
print(MyClass.__dict__)
'''


'''
MyClass = type('Foo',(),{'var1':'10','var2':'20'})
obj = MyClass()
print(obj.var1, obj.var2)
'''


class UpperAttrMetaclass(type):
        
    def __new__(cls,cname,bases,det):
        upperattr = {}
        
        for name,val in det.items():
            if not name.startswith('__'):
                upperattr[name.upper()]=val
            else:
                upperattr[name]=val
        
        return type.__new__(cls,cname,bases,upperattr)


class MyClass(metaclass=UpperAttrMetaclass):
    x = 10
    y = 20
    def myfunc():
        print('This is my func')




















