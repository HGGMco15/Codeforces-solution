import math
t=int(input())
for x in range(t):
    n=int(input())
    if n%2!=0:
        print("YES")
    else:
        c=math.log(n,2)
        if int(c)<c:
            print("YES")
        else:
            print("NO")
