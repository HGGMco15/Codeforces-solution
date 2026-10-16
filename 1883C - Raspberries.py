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
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if math.prod(a)%k==0:
        print(0)
    elif k==4:
        t1=1e9
        t2=1e9
        d=[]
        c=0
        for y in range(len(a)):
            if a[y]%2==0:
                c+=1
            d.append((4-a[y]%4)%4)
        t1=min(d)
        t2=0 if c>=2 else (1 if c==1 else 2)
        print(min(t1,t2))
    else:
        dp=1e12
        d=[]
        for y in range(len(a)):
            rb=a[y]
            d.append((k-a[y]%k)%k)
        print(min(d))
