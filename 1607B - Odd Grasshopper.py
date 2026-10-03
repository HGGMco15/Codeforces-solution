#Code by HGGMco15
#Module
from collections import Counter,defaultdict
import itertools
import math
import sys
#Fast I/O
input=sys.stdin.readline
#Custom function
def inp():
    sys.stdin=open("","r")
    sys.stdout=open("","w") 
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
t=int(input())
for x in range(t):
    a,n=map(int,input().split())
    if n%4==1:
        d=-n
    elif n%4==2:
        d=1
    elif n%4==3:
        d=n+1
    else:
        d=0
    if a%2==0:
        print(a+d)
    else:
        print(a-d)
