import math
n,m=map(int,input().split())
ls=[]
for x in range(1,n+1):
    ls.append(x)
d=sum(ls)
c=m%d
e,i=m//d,0
cout=m-(d*e)
while cout>0:
    cout-=ls[i]
    if cout-ls[i+1]<0:
        break
    i+=1
print(cout)
