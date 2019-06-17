# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 20:38:50 2019

@author: ggebr
Assignment-2
Write a python program that reads a text file, scramble the words in the file as per the rules 
given below and write the output to the new text file named by appending the word 'scrabble' 
to input filename (Consider your own text file as a input).

"""

import random
path = 'C:\\2019\\python\\'
inputFile ='lines.txt'
f = open(path + inputFile, 'r')

outpufile = 'scrabble' + inputFile
file = open(path + outpufile, 'w')
linesRead = f.readlines()

'''
Global initialization
'''
listwords = []
firstcharacter = ""
lastcharacter = ""
secondlastword = ""
lenghtofword = 0
lengthofline = 0
specialchars = ('.',';','?',',','!')
specialcharsflag = False
endofline = -1

#Apply Rule1 - Words less than or equal to 3 characters need not be scrabbled.
"""
 islessthan3wordslength - handle rule that stats that Words less than or equal to
 3 characters need not be scrabbled.
 input: str word
 input str file
 return: True
"""

def islessthan3wordslength(word, file):
    print("islessthan3wordslength entry:")
    if (len(word) <= 3):
        file.write(word + " ")
        file.write('\n')
        return True
'''
handlespecialcharacters - handle special charactes like ('.',';','?',',','!')
input: listwords,file,firstcharacter,secondlastword,lastcharacter

'''

def handlespecialcharacters(listwords,file,firstcharacter,secondlastword,lastcharacter):
        print("handlespecialcharacters entry:")  
        random.shuffle(listwords)
        file.write(firstcharacter + str(listwords) + secondlastword + lastcharacter) 
        file.write('\n')
       
def applyRule2(listwords):
      print("applyRule2 entry:")
      listwords.pop()
      listwords.pop()
                
for line in linesRead:
    print("line -->" + line)
    endofline = line.find("\n")
    lengthofline = len(line)
       
    for word in line.split():
        print("word->" + word)
        if islessthan3wordslength(word, file):
            continue
            
        loopcount = 0
        for ch in word:
            if loopcount ==0:
              firstcharacter = word[0]  
              lastcharacter = word[len(word) - 1]
              #lenghtofword = len(word) - 1
              loopcount += 1
              continue
              
            listwords.append(ch)
           
            if listwords[-1] == lastcharacter and lastcharacter in specialchars:
                #Apply Rule 3. Handle Special characters as last characters 
                secondlastword = listwords[-2]
                applyRule2(listwords)
                specialcharsflag = True
            elif listwords[-1] == lastcharacter:
                listwords.pop()
        if specialcharsflag:
                handlespecialcharacters(listwords,file,firstcharacter,secondlastword,lastcharacter)
                listwords = []
            
        else:
            "Waht  are we doing here??"
            random.shuffle(listwords)   
            file.write(firstcharacter + str(listwords) + lastcharacter )   
            listwords = []
            if endofline < lengthofline - 1:
                file.write(',')
                
            else:
                file.write('\n')
                endofline = 0
                lengthofline = 0
                print("finally")
                listwords = []
                
f.close()
file.close()







"""

s = 'sakeeb' 
mylist = list(s)
random.shuffle(mylist)  
print(mylist)

file.write(str(mylist))

f.close()
file.close()
"""