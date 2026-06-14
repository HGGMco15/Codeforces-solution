s=str(input())
countlower=0
countupper=0
for x in range(len(s)):
    if s[x].isupper():
        countupper+=1
    else:
        countlower+=1

if countupper>countlower:
    print(s.upper())
else:
    print(s.lower())
