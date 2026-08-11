t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    c=[]
    for x in a:
        if x==max(a):
            c.append(x)
        else:
            b.append(x)
    if len(b)==0 or len(c)==0:
        print(-1)
    else:
        print(len(b),len(c))
        print(*b)
        print(*c)
