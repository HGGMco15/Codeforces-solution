s=input()
n=int(input())
ls=[]
for x in range(n):
    s1=input()
    ls.append(s1)
ls.sort()
for y in ls:
    if len(y)>=len(s):
        c=y[0:len(s)]
        if c==s:
            print(y)
            break
else:
    print(s)
