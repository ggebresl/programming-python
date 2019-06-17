# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:49:51 2019

@author: ggebr
"""

import math
print (round(2.9))


print(math.ceil(2.2))

x = 1
y = x + 2
print(f"x: {x}, y:{y}")

print(ord('a'))
print(ord('A'))

age = 31

message =  "Eligible" if age >= 33 else "Not Eligible"
print(message)
#Iterable
for ch in "python":
   print(ch)
   
   counter = 0
   for number in range(1,10):
       if number % 2 == 0:
           counter += 1
           print(counter, number)

file =  open("C:\\2019\\python\\content.txt", "w")
file.write("This is the measse that is writen from the Python program")
file.close()
  
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        print(number, total)
    return total
    
multiply(2, 3, 4, 5)

def save_user( **user) :
    print(user)
save_user(id = 1, name='Gerawork', age = 54, profession = 'Engineer')


letters = ['a', 'b', 'c']
print(letters[-3])
zeros = [0] * 5
combined = letters + zeros 
print(combined)

print(set(range(5))) # you can do for list or tuple or set

leters = ['a', 'b', 'c', 'd']
print(leters[0:3])  #['a', 'b', 'c']
print(leters[:3])  #['a', 'b', 'c']

print(leters[0:])  # ['a', 'b', 'c', 'd']
print(leters[:])  # ['a', 'b', 'c', 'd']

nums = list(range(20))
print(nums)

print(nums[::2]) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print(nums[::3])  # [0, 3, 6, 9, 12, 15, 18]


print(nums[:-2]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

print(nums[::-2]) # [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]

print(nums[::-3])# [19, 16, 13, 10, 7, 4, 1]

leters2 = ['a', 'b', 'c', 'd']

for letter in enumerate(leters2):
    print(letter[0], letter[1])
   # print(letter)
   # (0, 'a')
   #(1, 'b')
   #(2, 'c')
   #(3, 'd') print(letter[0], letter[1])
    
fruit = ['apple', 'banana', 'cedar', 'dinna']
app_case_fruit = [f.upper() for f in fruit]
print(app_case_fruit)      

for letter in zip(leters2, fruit):
     print(letter[0], letter[1])
    
    #print(letter)
    #('a', 'apple')
   # ('b', 'banana')
   # ('c', 'cedar')
   # ('d', 'dinna')
   
   numb2 = [3, 5,51,8, 9]
   numb2.sort()
   print(numb2)
   
   items = [
            ("product1", 10),
            ("product2", 9),
            ("product3", 12)
           ]
   x = map(lambda item: item, items)
   
   for item in x:
       print(item)

filtered = list(filter(lambda item : item[1] >= 10, items))
print(filtered )


prices = [item[1] for item in items]
print(prices)

price = list(map(lambda item: item[1],  items))
print(price)


def square(x):
      return x**2
  
sq = map(square, range(11))
for s in sq:
    print(s)

squares = map(lambda x: x**2, range(10))
for s in squares:
    print(s)


 names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

 
lengths = map(len, names)

for len in lengths:
    print(len)
    
# zip functions
list1 = [1, 2, 3]
list2 =[10, 20, 30]

print(list(zip(list1, list2)))

#stacks
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

last = browsing_session.pop()
print(browsing_session)

browsing_session.append(-1)
print(browsing_session)

#queue
from collections import deque
queue = deque([])
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

queue.popleft()
print(queue)

if not queue:
    print("empty")


#array
    
from array import array

numbers = array("f", [1, 2, 3, 4])
print (numbers)
    
# let us create a set from an array
unique = set(numbers)
print(unique)


a = 20
b = a
if a is b:
    print('a = ', a, ', id(a) = ' ,id(a), 'b = ', b, ', id(b) = ',   id(b) )

else:
     print('a and b do not have the same identity')
     
# Unpacking operator
numbers = [1, 2, 3, 4]
print(numbers)
print(*numbers)

def main(x, y):
    if( x < y):
        st = "x is less than y"
    elif (x==y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"
    print(st)
   
if __name__ == "__main__": 
    main(1000, 100)
    main(100, 100)
    main(100, 1000)
    
    
    
class Point:
    default_color = "red"
    def __init__(self, x,y):
        self.x = x
        self.y = y
       
        
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
        
p = Point(1,2)
print(p.default_color)
p.draw()

#print(type(p))

#print(isinstance(p, Point))
#

dict = {1: "Gary", 2: "Ann", 3: "Stan"}
dict2 = dict
print(len(dict))

for key, val in dict.items():
    print(f"key = {key}, value = {val}")

dict[4] = "Stan"

lis = ()
for  l in dict.items():
    l.
f = dict.get(1)


for x in dict:
    print(dict[x])
    
dict.pop(2)

days = ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
daysEth = ["Ehud", "Segno", "Maksegno", "Rob", "Hamus", "Arb", "Kidame"]
for m in range(len(days)):
    print(m, days[m])

#you can use enumerate to reduces code and provides a coubter
    for i, m in enumerate(days, start=1):
        print(i, m)

# use zip to combine sequences
for m in zip(days, daysEth):
    print(m)
    

def main():
    #define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)


if n > 0 and n < 5:
    print('n is in range of 1 to 5')


#1
 age = int(input ("Enter your age")
     if age > 26:
         print("you are not allowed to be registered for selection service" )


#2

if condition:
    indented_statement(s)
[elif condition:
    indented_statement(s) ]

[else:
    indented_statements ]
    

    if n < 1:
        print('n is below range of 100')
        
    elif n < 101:
        print('n is inside the range')
        print("Thank you!")
    else:
        print(' n is above the the range 1 to 100')
        
#3
player_x = 0
player_y = 0

if keyboard.right:
    player_x += 5   
    
elif keyboard.left:
    player_x -= 5
    
elif keyboard.up:
    player_y += 5
    
elif keyboard.down:
    player_y -= 5
    
else:
    player_x += 180
    player_y -= 180
    
    

argument=4
options = {
           0 : "zero",
           1 : "one",
           4 : "four",
           9 : "nine",
           2 : "even",
           3 : "prime",
           5 : "prime",
           7 : "prime",
}

options.get(argument, "nothing")










