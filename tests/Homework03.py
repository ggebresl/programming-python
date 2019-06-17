# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 20:38:50 2019

@author: ggebr
Homework
"""


import random
#Global initialization

path = 'C:\\2019\\python\\'
inputFile ='lines.txt'
f = open(path + inputFile, 'r')

outpufile = 'scrabble' + inputFile
file = open(path + outpufile, 'w')

linesRead = f.readlines()

listwords = []
firstcharacter = ""
lastcharacter = ""
secondlastword = ""
lenghtofword = 0
lengthofline = 0
specialchars = ('.',';','?',',','!')
specialcharsflag = False
endofline = -1

linefromeachword ="";

for line in linesRead:
    print("line -->" + line)
    endofline = line.find("\n")
    lengthofline = len(line)
    listLine = list(line)
    print( str(listLine))
    print("length of line -> " + str(len(line)))
    print("NEWLINE-->" + line[endofline])
    print("endofline-->" + str(endofline))
    linefromeachword=""
    
    for word in line.split():
        #build up a line from the incoming word so we can compare it with the orginal line
        linefromeachword = linefromeachword + word + " "
        print("word-> " + word)
        if (len(word) <= 3):
            file.write(word + " ")
            print("islessthan3wordslength called")
            continue
        
        loopcount = 0
        #handle cases if length Words is greater than 3 characters 
        for ch in word:
            if loopcount == 0:
              firstcharacter = word[0]  
              lastcharacter = word[len(word) - 1]
              loopcount += 1
              continue
          
            listwords.append(ch) 
            if (listwords[-1] == lastcharacter and lastcharacter in specialchars):
                secondlastword = listwords[-2]
                listwords.pop()
                listwords.pop()
                specialcharsflag = True
            elif listwords[-1] == lastcharacter:
                listwords.pop()
                
            if specialcharsflag:
                random.shuffle(listwords)
                file.write(firstcharacter + str(listwords) + secondlastword + lastcharacter) 
                listwords = []
                file.write('\n')
                print("specialcharsflag")
                
            else:
                random.shuffle(listwords)   
                file.write(firstcharacter + str(listwords) + lastcharacter )   
                listwords = []
                
            #write a NEWLINE in the output, if we are at the end of the line
            if len(linefromeachword) == len(line):
                print("we are at else1")
                print(linefromeachword)
                print(line)
                file.write('\n')   
                listwords = []
            else:
                print("we are at elsee")
                file.write(',')
                endofline = 0
                lengthofline = 0
                listwords = []
                
   # listwords = []
f.close()
file.close()



s = 'sakeeb' 
mylist = list(s)
random.shuffle(mylist)  
print(mylist)

file.write(str(mylist))

f.close()
file.close()
