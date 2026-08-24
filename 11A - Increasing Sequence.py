import math
n,d=map(int,input().split())
a=list(map(int,input().split()))
cout=0
for x in range(len(a)-1):
    if a[x]>=a[x+1]:
        if a[x]==a[x+1]:
            a[x+1]=a[x+1]+d
            cout+=1
        else:
            c=a[x]+1-a[x+1]
            a[x+1]=a[x+1]+(d*math.ceil(c/d))
            cout+=math.ceil(c/d)
print(cout)
