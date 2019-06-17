# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:52:23 2019

@author: ggebr
"""
# integer and float ype conversion
import math
print(f"The data type of type(3) is {type(3)}")
print(f"The data type of type(3.5) is {type(3.5)}")

print(f"Convert 3.5 to integer --> {int(3.5)}")
print(f"Convert integer 3 to float --> {float(3)}")

#strings
username = "ggebresl"
password = "kidan321"
msg = "welcome {}, {} !".format(username, password)
print(msg)

name = 'gerawork gebreslassie'
print(name.title())    #Gerawork Gebreslassie
print(name.upper())
full_name = "GERAWORK GEBRESLASSIE".lower()
print(full_name)

Name = '   Hello Wold   '
print(Name.lstrip())
print(Name.rstrip())
print(name.strip())

# numbers
print(round(3.1234567,2))
print(round(31.1234567,-1))
print(round(312.1234567,-2))
print(round(312.1234567,2))

math.log(100,10)
math.log(1000,10)
math.log(10000,10)

math.log(1000000,10)
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    contents = contents.replace('\n','')
    print(contents)
    # let us study about lists
    
vowels =  [ 'e', 'i', 'o'] 
print(vowels[0])  # access list itesm through their posion in the list
print(vowels[-1])  $ last elemet

vowels.append('u') # add single item at the end

vowels.insert(0, 'a') # insert item at a give posion

vowels[-1] = 'y' # modify an elemetin a list using index

vowels = ['a','u', 'e', 'i', 'o', 'y']
sorted(vowels) # ['a', 'e', 'i', 'o', 'u', 'y'] (please note this is the output without affecting the variable vowels. It is just a sorted temp output)

vowels.sort() # this permanently sorts the variable vowels
vowels.reverse() # --> ['y', 'u', 'o', 'i', 'e', 'a']

nums = [1, 3, 2, 4]
sorted(nums)
airports = ['ANS','JNU', 'SEA', 'SIT']

airports.remove('SEA')  # remove specfic item in a list
del airports[1]   # deletes at item at a specific postion in the list using index

air_ports = ['ANS','JNU', 'SEA', 'SIT']
airport = air_ports.pop() # removes and returns the last item in a list
aport = air_ports.pop(0) # rturns SEA . can also accept an index

#A slice is part of a list that begins with the item at the first index specified and stops with item beofe the last index specfied

states = ['CA', 'CO', 'CT', 'DE', 'FL', 'GA']
sts = states[2:4] #--> ['CT', 'DE'] # get range from 2 to 4 but not includig 4

st = states[:2] # omit the first index, and the slice starts with the first item in the list--> ['CA', 'CO']
s = states[3:] # omit the second index, and the slice goes to the end of the list. -->['DE', 'FL', 'GA']

first_two_items = states[:2] #-->['CA', 'CO']
last_two_items = states[-2:] # -->['FL', 'GA']
range_of_items = states[2:4] # -->['CT', 'DE']


# A copy of lists let you work the contents of the copied list without affecting the the original list
# Make a copy of a list by slicing while omittig both indexes. This generates a slice from the star to the end of the list

usaStates = ['CA', 'CO', 'CT','DE']
myStates = usaStates[:] #--> ['CA', 'CO', 'CT', 'DE']

myStates.append('NH') --> ['CA', 'CO', 'CT', 'DE', 'NH', 'NH']. However usaStats are stil have --> 'CA', 'CO', 'CT', 'DE']

for state in myStates:
    print(state)
    
for s in myStates[:2]: #Loop throught part of a list
    print(s)  > CA, CO
    
#The rarnge() function generates a series of numbers from 0 upto, but not including, the number
numbers = list(range(5))# outputL--> [0, 1, 2, 3, 4]
high_numbers = list(range(95,100)) #--> [95, 96, 97, 98, 99]

odds = list(range(1, 10, 2)) #-->[1, 3, 5, 7, 9]

#To define a pattern, make an empty list and then modify each number in a range. This lists the power of 10
nums = []
for exp in range(5):
    nums.append(10**exp) #-->[1, 10, 100, 1000, 10000]
    
# A list comprehension is a compact way of defining a list in one line
 ns =  [ 10 **exp for exp in range(5)] #-->[1, 10, 100, 1000, 10000]
 
 #Tupple- A tupple is an ordered collection of items that can't be modified. It is usually indicated by parenthesis:
 elementary_grades = [4, 5, 6]
 
 grade4 =elementary_grades[0] #Elements in a tupple are accessed using indexes
 grade5 = elementary_grades[1]
 grade6 = elementary_grades[2]

filename = 'programming.txt'
with open(filename, 'w') as fileobj:
    fileobj.write("Programming is fun")
    print('wrting to programming.txt is done. Check it')
    
# wite a list ot a json file
import json
numbers = [1, 2, 3, 4, 5, 6, 7]
fname = 'numbers.json'

with open(fname, 'w') as fobj:
    json.dump(numbers, fobj)
    print("numbers.json is generated")
    
# read json file to memory
import json

fn = 'numbers.json'

with open(fn) as fobj:
    numbers = json.load(fobj)
    print(numbers )
    
#Start of Dictionary Dtatype**********************************************************************************
# A dictionary is a set of items;each item consists of a key and a value .You define a dictionary using braces
    
capitals = {
        'MA': 'Massachussetts',
        'NY' : 'New Yourk',
        'NH' : 'New Hampshier',
        'CA' : 'California'
        
        }
# ADD itmes to an existing dictionary by placig the new key in brackets and providing the value
capitals['WA'] = 'Washington DC'
del capitals['NH']

#the get() method returned the value associated with a key if that key exists in the dictionary, else None. you can also pass a default 
#value to be returned if the key doesn't exist.

caState = capitals.get('CA') 
noState = capitals.get('GA', 'unknown') # uf the key or 'GA' does not exist return 'unknown'

capitals.keys() #-> dict_keys(['MA', 'NY', 'NH', 'CA', 'WA'])
capitals.values()#->dict_values(['Massachussetts', 'New Yourk', 'New Hampshier', 'California', 'Washington DC'])
capitals.items() #-> dict_items([('MA', 'Massachussetts'), ('NY', 'New Yourk'), ('NH', 'New Hampshier'), ('CA', 'California'), ('WA', 'Washington DC')])

capitals.clear() #->  {}  empty the dictionary
copiedDict = capitals.copy() # coiedDict gets a shallow copy of capitals. The same key/value are copied to copiedDict
capitals.__doc__

# A dictionary key can be associated with a list of values:
state_visited = {
        'gerwork' : ['GA', 'NY', 'DC', 'MN'],
        'abeba' : ['WA','NC', 'GA']
        }
#when  you loop through the items, each value will be a list.To do this, nest a for loop for list inside a for loop for the dictionary:

for key, values in state_visited.items():
    print(f"{key} has visited")
    print("---------------------")
    for val in values:
        print(f"{val}")
    print('\n')

#End of Dictionary Dtatype*****************************************************************************
    
    
    
    
    
    
    
    
    
    
    
    
    
    