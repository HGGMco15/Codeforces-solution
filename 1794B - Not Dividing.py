t=int(input())
for c in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for x in range(len(a)):
        if a[x]==1:
            a[x]+=1
    for x in range(1,len(a)):
        if a[x]%a[x-1]==0:
            a[x]+=1
    print(*a)
