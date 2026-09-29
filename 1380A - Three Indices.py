from collections import Counter,defaultdict
import itertools
import math
import sys
input=sys.stdin.readline
t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for y in range(1,n-1):
        if a[y]>a[y-1] and a[y]>a[y+1]:
            print("YES")
            print(y,y+1,y+2)
            break
    else:
        print("NO")
