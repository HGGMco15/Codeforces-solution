#Code by HGGMco15 (Free to read but not copy)
#Module
from collections import Counter,defaultdict
import bisect
import itertools
import math
import sys
#Fast I/O & Set-up
input=sys.stdin.readline
#Custom function
def inp(flag):
    if flag:
        sys.stdin=open("","r")
        sys.stdout=open("","w")
def palindrome(s):
    return s==s[::-1] 
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
def binary_search(ar,tar):
    lo,hi=0,len(ar)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if ar[mid]==tar:
            return mid
        else:
            if ar[mid]<tar:
                lo=mid+1
            else:
                hi=mid-1
    return -1
def binary_search_dup(ar,tar,flag):
    if flag:
        return bisect.bisect_left(ar,tar)
    if (bisect.bisect_right(ar,tar)-1)>0 and ar[bisect.bisect_right(ar,tar)-1]==tar:
        return bisect.bisect_right(ar,tar)-1
    return 1
#Main
t=int(input())
for x in range(t):
    s=input()
    if len(s)==1:
        print(1)
    else:
        s1=s.count("1")
        s2=s.count("0")
        print(next((len(s.strip())-i for i, c in enumerate(s.strip()) if (c=='0' and (s1:=s1-1)<0) or (c=='1' and (s2:=s2-1)<0)), 0))
