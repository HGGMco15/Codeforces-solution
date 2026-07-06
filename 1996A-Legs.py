import math
t=int(input())
ans=[]
for x in range(t):
    n=int(input())
    if n<4:
        ans.append(math.floor(n/2))
    elif n==4:
        ans.append(1)
    else:
        if n%4==0:
            ans.append(n//4)
        else:
            ans.append(math.floor(n/4)+1)
for p in ans:
    print(p)
