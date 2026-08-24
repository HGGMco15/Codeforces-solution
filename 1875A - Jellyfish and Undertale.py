t=int(input())
for c in range(t):
    a,b,n=map(int,input().split())
    x=list(map(int,input().split()))
    r=0
    for i in range(n):
        r+=min(a-1,x[i])
    print(r+b)
