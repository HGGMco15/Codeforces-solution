import math
t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ls=[]
    for y in range(len(a)):
        ls.append(abs(a[y]-y-1))
    print(math.gcd(*ls))
