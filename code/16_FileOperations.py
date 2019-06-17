'''
open(<filepath>,<filemode>)
Filemode - r, w, a, rb, wb
'''
#reading file
'''
f = open('inp.txt','r')
data = f.read()
print(data)
f.close()
'''
#writing a file
'''
f = open('inp.txt','a')

f.write('This is new content that i want to write')

f.close()
'''

f = open('inp.txt','r')
data = f.readlines()
for line in data:
    print(line.split())
f.close()








