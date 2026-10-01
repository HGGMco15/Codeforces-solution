#Code by HGGMco15
#Module
from collections import Counter,defaultdict
import itertools
import math
import sys
#Custom function
def prime(s):
    if s<2:
        return False
    if s<4:
        return True
    if s%2==0 or s%3==0:
        return False
    i=5
    while i*i<=s:
        if s%i==0 or s%(i+2)==0:
            return False
        i+=6
    return True
#Main
input=sys.stdin.readline
n,k=map(int,input().split())
ls=[]
for x in range(2,n+1):
    if prime(x):
        ls.append(x)
for x in range(2,n+1):
    for y in range(len(ls)-1):
        if (ls[y]+ls[y+1]+1)==x and prime(x):
            k-=1
            break
if k>0:
    print("NO")
else:
    print("YES")
