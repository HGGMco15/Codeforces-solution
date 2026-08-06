t=int(input())
for x in range(t):
    a,b,c=map(int,input().split())
    ls=[]
    ls.append(a)
    ls.append(b)
    ls.append(c)
    ls.sort()
    if a==b or a==c or c==b:
        print(0)
    else:
        print(min(ls[2]-ls[1],ls[1]-ls[0]))
