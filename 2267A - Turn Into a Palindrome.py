import math
def pal(s):
    return s==s[::-1]
t=int(input())
for x in range(t):
    n,c=map(str,input().split())
    n=int(n)
    s=input()
    if pal(s):
        print(0)
    else:
        cout=0
        lo=0
        hi=n-1
        d=math.floor(n/2)
        for y in range(d):
            if s[lo]!=s[hi]:
                if s[lo]==c or s[hi]==c:
                    cout+=1
                else:
                    cout+=2
            lo+=1
            hi-=1
        print(cout)
