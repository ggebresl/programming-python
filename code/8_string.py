#
s = 'B2A1D3C4'
alp = []
num = []
for ch in s:
    if ch.isalpha():
        alp.append(ch)
    else:
        num.append(ch)
alp.sort()
num.sort()
print(alp)
print(num)
alp.extend(num)
print(''.join(alp))

s1=s2=final=''
for ch in s:
    if ch.isalpha():
        s1+=ch
    else:
        s2+=ch
output = ''.join(sorted(s1)+sorted(s2))
print(output)
