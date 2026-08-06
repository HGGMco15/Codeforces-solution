n=int(input())
a=list(map(int,input().split()))
q=int(input())
a.sort()
for x in range(q):
    m=int(input())
    ans=0
    lo=0
    hi=len(a)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if a[mid]<=m:
            ans+=mid #you can remove this if you want (My first time learning binary search btw)
            lo=mid+1
        else:
            hi=mid-1
    print(lo)
