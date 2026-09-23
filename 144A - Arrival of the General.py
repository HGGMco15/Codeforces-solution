n=int(input())
a=list(map(int,input().split()))
c,d=max(a),min(a)
lo=0
hi=n-1
while a[lo]!=max(a):
    lo+=1
while a[hi]!=min(a):
    hi-=1
if lo==hi:
    print(0)
else:
    if lo<hi:
        print(lo+(n-1-hi))
    else:
        for x in range(lo,0,-1):
            a[x],a[x-1]=a[x-1],a[x]
        hi=n-1
        while a[hi]!=min(a):
            hi-=1
        print(lo+(n-1-hi))
