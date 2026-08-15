import math
t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if len(a)==1:
        print(0)
    else:
        cout=0
        for y in range(n-1):
            if (a[y]%2==0 and a[y+1]%2==0) or (a[y]%2!=0 and a[y+1]%2!=0):
                cout+=1
        print(cout)
