n=int(input())
ls=[]
ls2=[]
for x in range(n):
    c,d=map(int,input().split())
    ls.append(c)
    ls2.append(d)
for x in range(len(ls)):
    if ls[x]+ls2[x] in ls:
        f=ls.index(ls[x]+ls2[x])
        if ls[f]+ls2[f]==ls[x]:
            print("YES")
            break
else:
    print("NO")
