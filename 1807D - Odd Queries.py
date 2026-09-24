import math
t=int(input())
for x in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    b=a
    pref=[0]*(n+1)
    for y in range(n):
        pref[y+1]=pref[y]+b[y]
    d=pref[len(pref)-1]
    for y in range(q):
        l,r,k=map(int,input().split())
        num=r-l+1
        f=num*k
        sm=pref[r]-pref[l-1]
        if (d-sm+f)%2==0:
            print("NO")
        else:
            print("YES")
