n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
cout=0
for x in range(m):
    if a[x]<0:
        cout+=a[x]
print(abs(cout))
