t=int(input())
for x in range(t):
    n=int(input())
    a=input()
    mxlen=len(a)
    r=len(a)-1
    l=0
    for y in range(n):
        if a[r]==a[l] or l==r:
            break
        mxlen-=2
        r-=1
        l+=1
    if mxlen>=0:
        print(mxlen)
    else:
        print(0)
