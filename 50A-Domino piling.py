import math
n,m=map(int,input().split())
a=n*m
if a%2==0:
    print(int(a/2))
else:
    print(int(math.floor(a/2)))
