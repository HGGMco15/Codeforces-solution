import math
def base(a,b):
    sm=0
    while a>0:
        sm+=a%b
        a=a//b
    return sm
n=int(input())
ls=[]
for x in range(2,n):
    ls.append(base(n,x))
d=sum(ls)
c=math.gcd(d,len(ls))
print(f"{d//c}/{len(ls)//c}")
