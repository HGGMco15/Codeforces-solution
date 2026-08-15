import math
t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=False
    for i in range(n):
        for j in range(n):
            if i!=j:
                if math.gcd(a[i],a[j])<=2:
                    c=True
    if c:
        print("Yes")
    else:
        print("No")
