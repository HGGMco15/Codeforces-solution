t=int(input())
for x in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    cout=1
    ans=1
    for i in range(1,n):
        if a[i]-a[i-1]<=k:
            cout+=1
        else:
            cout=1
        if cout>ans:
            ans=cout
    print(n-ans)
