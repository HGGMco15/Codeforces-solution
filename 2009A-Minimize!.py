t=int(input())
ans=[]
for x in range(t):
    a,b=map(int,input().split())
    if a==b:
        ans.append(0)
    else:
        cur=10000000000
        sums=0
        for x in range(a,b+1):
            sums=(x-a)+(b-x)
            if cur>sums:
                cur=sums
        ans.append(cur)
for p in ans:
    print(p)
