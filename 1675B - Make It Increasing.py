import math
t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if a==sorted(a) and len(set(a))==len(a):
        print(0)
    else:
        cout=0
        prev=a[n-1]
        for y in range(len(a)-2,-1,-1):
            if prev<=a[y]:
                while (a[y]>=prev) and (a[y]>0):
                    a[y]=math.floor(a[y]/2)
                    cout+=1
            prev=a[y]
        if len(set(a))!=n:
            print(-1)
        else:
            print(cout)
