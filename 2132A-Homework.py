t=int(input())
ans=[]
for x in range(t):
    n=int(input())
    a=str(input())
    m=int(input())
    b=str(input())
    c=str(input())
    ls=[]
    for m in range(len(a)):
        ls.append(a[m])
        
    for y in range(len(c)):
        if c[y]=="V":
            ls.insert(0,b[y])
        else:
            ls.insert(len(ls),b[y])
    d="".join(ls)
    ans.append(d)

for p in ans:
    print(p)
