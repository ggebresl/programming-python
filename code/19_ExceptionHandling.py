'''
ZeroDivisionError
NameError
TypeError
ValueError
'''
#try, except, finally, else
'''
try:
    a = int(input('enter a number'))
    #if a==10:
#        raise ValueError('The Number 10 is not allowed')
    c = b/a
    print(c)

except TypeError:
    print('This Is TypeError')
except ValueError:
    print('The Number 10 is not allowed')
except ZeroDivisionError:
    print('This is ZeroDivideError')
except NameError:
    print('This is NameError')
else:
    print('Code executed Successfully')
finally:
    print('This code always gets executed')
'''

'''
try:
    a = int(input('enter a number'))
    c = 10/a
    print(c)
finally:
    print('This code always gets executed')
'''
'''
raise => 
assert
  ''' 
#Nested try,except,finally,else  
try:
    try:
        try:
            #some code
        except:
            #some code

    except:
        #some code
except:
    #some code
    try:
        #some code
    except:
        #some code
else:
    try:
        #some code
    except:
        #some code








