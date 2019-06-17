'''
--string methods
count,endswith, startswith, index, isalnum,isalpha,
isdecimal, islower, isupper, lower, upper, strip, join,
replace, split, splitlines, chr, ord
--Special functions
    eval, zip, enumerate
--comprehensions
    list,dictionary,set
--functions and type of arguments, scope of a variable
    First class Citizen
--Anonymeous Functions
    lambda, map, filter, reduce
--File Handling
    working with csv file
'''

#1. String methods
#s = 'sakeeb'
'''
print(len(s))
l = [1,2,3,4,5,6,7,8,9]
print(len(l))
'''

#1. count
'''
print(s.count('e'))
print(s.count('a'))
print(s.count('sak'))
'''

#2. index()
'''
s = 'sakeeb'
print(s.index('a'))
print(s.index('e'))
'''
#3. startswith(), endswith()
#str1 = "playing played plays moving jumping eating matching"
#print(str1.startswith('play'))
#print(str1.endswith('ing'))

#4.split()
str1 = """playing played    plays moving 


jumping eating matching"""
'''
list_str = str1.split()
print(list_str)

for word in list_str:
    if word.endswith('ing'):
        print(word)

for word in list_str:
    if word.startswith('play'):
        print(word)        

s = "playing,played,plays,moving,jumping,eating,matching"
li = s.split(',')
print(li)
'''

#isalnum(), isalpha(), isdecimal()
'''
s = 'jamesbond007'
print(s.isalnum())
 
s = 'sakeeb'
print(s.isalpha())  

s = '12345'
print(s.isdecimal())
'''

#lower, upper, islower, isupper
'''
s = 'sakeeb'
print(s.upper())

s = 'Sakeeb'
print(s.lower())

s = 'Sakeeb'
print(s.islower())

s = 'Sakeeb'
print(s.islower())

s = 'SAKEEB'
print(s.isupper())
'''

#join
'''
s = 'SAKEEB'
li = list(s)
print(li)
print(','.join(li))
'''

#chr() and ord()
print(chr(66))
print(ord('B'))





















