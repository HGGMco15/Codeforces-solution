t=int(input())
for x in range(t):
    n,k=map(int,input().split())
    a=list(input())
    b=set(a)
    cout=0
    for x in b:
        if a.count(x)%2!=0:
            cout+=1
    if cout>k+1:
        print("NO")
    else:
        print("YES")
