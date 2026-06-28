t=int(input())
ans=[]
for x in range(t):
    x,n=map(int,input().split())
    if n%2==0:
        ans.append(0)
    else:
        ans.append(x)
for p in ans:
    print(p)
