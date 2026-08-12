t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cout=0
    mxcout=0
    for y in a:
        if y==0:
            cout+=1
        else:
            if mxcout<cout:
                mxcout=cout
            cout=0
        if mxcout<cout:
            mxcout=cout
    print(mxcout)
