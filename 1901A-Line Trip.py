t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    maxdif=-1e9
    for l in range(n-1):
        maxdif=max(maxdif,abs(a[l]-a[l+1]))
    tg=(x-a[len(a)-1])*2
    print(max(maxdif,tg,a[0]))
