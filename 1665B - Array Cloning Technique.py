from collections import Counter,defaultdict
import math
import random
import sys
input=sys.stdin.readline
t=int(input())
ans=[]
rd=random.randint(1,10**9)
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=Counter(x^rd for x in a)
    e=max(b.values())
    if e==n:
        ans.append("0")
    else:
        f=n-e
        cout=0
        while f>0:
            cout+=1
            e*=2
            f-=e//2
            if f<0:
                cout+=e//2+f
                break
            else:
                cout+=e//2
        ans.append(str(cout))
print("\n".join(ans))
