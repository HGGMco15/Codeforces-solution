import math
y,w=map(int,input().split())

prob=6-max(y,w)+1

if 6%prob!=0:
    ans=math.gcd(prob,6)
    print(f"{int(prob/ans)}/{int(6/ans)}")
else:
    print(f"{int(prob/prob)}/{int(6/prob)}")
