t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n%2!=0:
        xr=0
        for y in range(n):
            xr^=a[y]
        print(xr)
    else:
        xr=0
        for y in range(n):
            xr^=a[y]
        if xr==0:
            print(0)
        else:
            print(-1)
