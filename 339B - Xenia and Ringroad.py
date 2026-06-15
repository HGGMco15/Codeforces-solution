n,m=map(int,input().split())
a=list(map(int,input().split()))
count=0
cur=1
for x in range(len(a)):
    if a[x]>=cur:
        count+=a[x]-cur
        cur=a[x]
    else:
        count+=n-cur+a[x]
        cur=a[x]
 
print(count)
