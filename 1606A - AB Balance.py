from collections import Counter,defaultdict
import itertools
import math
import sys
input=sys.stdin.readline
t=int(input())
ans=[]
for x in range(t):
    s=input().strip()
    if s[0]==s[len(s)-1]:
        ans.append(s.strip())
    else:
        c,d="",""
        if s[0]=="b":
            for y in range(len(s)):
                if y==0:
                    c+="a"
                else:
                    c+=s[y]
            for y in range(len(s)):
                if y==len(s)-1:
                    d+="b"
                else:
                    d+=s[y]
            l=c.count("ab")
            r=c.count("ba")
            l1=d.count("ab")
            l2=d.count("ba")
            if l==r:
                ans.append(c.strip())
            else:
                ans.append(d.strip())
        else:
            for y in range(len(s)):
                if y==0:
                    c+="b"
                else:
                    c+=s[y]
            for y in range(len(s)):
                if y==len(s)-1:
                    d+="a"
                else:
                    d+=s[y]
            l=c.count("ab")
            r=c.count("ba")
            l1=d.count("ab")
            l2=d.count("ba")
            if l==r:
                ans.append(c.strip())
            else:
                ans.append(d.strip())
print("\n".join(ans))
