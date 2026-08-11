t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if a==sorted(a):
        g=0
        req=0
        o=1e9
        for y in range(n-1):
            if a[y]<=a[y+1]:
                g=a[y+1]-a[y]
                req=g//2+1
                o=min(req,o)
        print(o)
    else:
        print(0)
