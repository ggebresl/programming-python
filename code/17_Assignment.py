'''
Write a python program that reads a text file, scramble the words 
in the file as per the rules given below and write the output to 
the new text file named by appending the word 'scrabble' to input 
filename (Consider your own text file as a input).

RULES:
	1. Words less than or equal to 3 characters need not be scrabbled.
	2. Don't scrabble first and last character.
	3. Special characters as last characters are to be maintained as it is. Special characters 
                like ( . , ; , ? ,,  !)  eg:- National. (here last two characters to be kept as it is.)
	4. Maintain sequence of line of text file.
	5. Use functions, modules as per requirement.
	6. It should be based on functionality, coding standards, modularity.
	7. Functionality like number of lines, number of words, vowels in the text file.
'''
from random import shuffle
f = open('../input/input.txt','r')
data = f.readlines()
f.close()
symb = ''',.?/{}[]()-+=!'"@#$%^&*~'''
finaldata = []
for line in data:
    wL = line.split()
    finalline = ''
    #print(wL)
    for word in wL:
        issplchar = 0
        #print(word)
        if len(word)>3:
            if word[-1] in symb:
                w1 = word[1:-2]
                issplchar = 1
            else:
                w1 = word[1:-1]
            #print(w1)
            cL = list(w1)
            #print(cL)
            shuffle(cL)
            #print(cL)
            #print(''.join(cL))
            #print(word[0] + ''.join(cL) + word[-1])
            if issplchar==1:
                w2 = word[0] + ''.join(cL) + word[-2] + word[-1]
            else:
                w2 = word[0] + ''.join(cL) + word[-1]
                
                
            finalline = finalline + w2 + ' '
        
        else:
            #print(word)
            finalline = finalline + word + ' '
    
    finaldata.append(finalline+'\n')    
#print(finaldata)


f = open('../input/input_scrubble.txt','w')
f.writelines(finaldata)
f.close()
        
















