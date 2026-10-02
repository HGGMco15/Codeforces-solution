#Code by HGGMco15
#Module
from collections import Counter,defaultdict
import itertools
import math
import sys
#Fast I/O
input=sys.stdin.readline
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
t=int(input())
for x in range(t):
    a,b,c=map(int,input().split())
    if (2*b-c>=a and (2*b-c)%a==0 and (2*b-c)!=0):
        print("YES")
    elif ((a+c)//2>=b and ((a+c)//2)%b==0 and ((a+c)//2)!=0 and (a+c)%2==0):
        print("YES")
    elif (2*b-a>=c and (2*b-a)%c==0 and (2*b-a)!=0):
        print("YES")
    else:
        print("NO")
