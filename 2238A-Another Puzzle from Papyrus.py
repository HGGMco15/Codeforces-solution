t=int(input())
ans=[]
 
for _ in range(t):
 n,c=map(int,input().split())
 a=list(map(int,input().split()))
 b=list(map(int,input().split()))
 
 inf=10**18
 res=inf
 
 ok=1
 cost=0
 
 for i in range(n):
  if a[i]<b[i]:
   ok=0
   break
  cost+=a[i]-b[i]
 
 if ok:
  res=min(res,cost)
 
 a.sort(reverse=True)
 b.sort(reverse=True)
 
 ok=1
 cost=c
 
 for i in range(n):
  if a[i]<b[i]:
   ok=0
   break
  cost+=a[i]-b[i]
 
 if ok:
  res=min(res,cost)
 
 if res==inf:
  ans.append(-1)
 else:
  ans.append(res)
 
for x in ans:
 print(x)
