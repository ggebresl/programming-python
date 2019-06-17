'''
#Input :-B2A1D3C4
#Output :- ABCD1234
s=input('Enter a Alfanumeric String')
s1=s2=output=''
for i in s:
    if i.isalpha():
        s1=s1+i
    else:
        s2=s2+i
print(''.join(sorted(s1))+''.join(sorted(s2)))
#OR
print(''.join(sorted(s1)+sorted(s2)))


#Input :-a4b3
#Output :- aaaabbb
s=input('Enter a Alfanumeric String')
output=''
for i in s:
    if i.isalpha():
        output=output+i
        previous = i
    else:
        output=output+previous*(int(i)-1)

print(output)


#Input :-a4b3
#Output :- aebe
s=input('Enter a Alfanumeric String')
output=''
for i in s:
    if i.isalpha():
        output=output+i
        previous = i
    else:
        output=output+chr(ord(previous)+(int(i)))

print(output)


#Input1 :- SAKEEB
#Input2 :- SHEIKH
#Output :- SSAHKEEIEKBH
s1=input('Enter a First String')
s2=input('Enter a Second String')
output=''
i=j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
    
print(output)
'''
