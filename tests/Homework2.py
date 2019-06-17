# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 20:38:50 2019

@author: ggebr
Homework
"""

import sys
import random
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

for line in linesRead:
    print("line -->" + line)
    endofline = line.find("\n")
    lengthofline = len(line)
    print("length of line -> " + str(len(line)))
    print("NEWLINE-->" + line[endofline])
    print("endofline-->" + str(endofline))
    for word in line.split():
        print("word->" + word)
        if (len(word) <= 3):
            file.write(word)
            file.write('\n')
            continue
        loopcount = 0
        for ch in word:
            if loopcount ==0:
              firstcharacter = word[0]  
              lastcharacter = word[len(word) - 1]
              lenghtofword = len(word) - 1
              #print(firstcharacter)
              #print(lastcharacter)
              #print ("Length = " + str(lenghtofword))
              loopcount += 1
              continue
              
            listwords.append(ch)
            if listwords[-1] == lastcharacter and lastcharacter in specialchars:
                secondlastword = listwords[-2]
                #print("lastword" + listwords[-1])
                #print("secondlastword")
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
                
        else:
            random.shuffle(listwords)   
            file.write(firstcharacter + str(listwords) + lastcharacter )   
            listwords = []
            if endofline < lengthofline - 1:
                file.write(',')
                
            else:
                file.write('\n')
                endofline = 0
                lengthofline = 0
                
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
