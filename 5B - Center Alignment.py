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
data=list(sys.stdin.read().splitlines())
mxlen=0
turn="lft"
for x in data:
    mxlen=max(mxlen,len(x.strip()))
cache=mxlen+2
for x in range(len(data)+2):
    if x==0 or x==len(data)+1:
        for y in range(mxlen+2):
            print("*",end="")
        print()
    else:
        if len(data[x-1].strip())==0:
            st="*"
            for y in range(cache-2):
                st+=" "
            st+="*"
            print(st)
        else:
            if (mxlen-len(data[x-1].strip()))%2==0:
                space=cache-len(data[x-1].strip())-2
                st="*"
                for y in range(space//2 if space%2==0 else space//2):
                    st+=" "
                st+=data[x-1].strip()
                for y in range(space//2 if space%2==0 else space//2):
                    st+=" "
                st+="*"
                print(st)
            else:
                if turn=="lft":
                    space=cache-len(data[x-1].strip())-2
                    st="*"
                    for y in range(space//2):
                        st+=" "
                    st+=data[x-1].strip()
                    for y in range(space//2+1 if (len(data[x-1].strip())>1) or (mxlen>1) else space//2):
                        st+=" "
                    st+="*"
                    print(st)
                else:
                    space=cache-len(data[x-1].strip())-2
                    st="*"
                    for y in range(space//2+1 if (len(data[x-1].strip())>1) or (mxlen>1) else space//2):
                        st+=" "
                    st+=data[x-1].strip()
                    for y in range(space//2):
                        st+=" "
                    st+="*"
                    print(st)
                turn="lft" if turn=="rgt" else "rgt"
