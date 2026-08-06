t=int(input())
for x in range(t):
    n=int(input())
    a=input()
    b=input()
    eva=[]
    odda=[]
    evb=[]
    oddb=[]
    for i in range(n):
        if a[i]=="1":
            if i%2==0:
                eva.append(i)
            else:
                odda.append(i)
        if b[i]=="1":
            if i%2==0:
                evb.append(i)
            else:
                oddb.append(i)
    if len(eva)!=len(evb) or len(odda)!=len(oddb):
        print(-1)
    else:
        ans=0
        for y in range(len(eva)):
            ans+=abs(eva[y]-evb[y])//2
        for y in range(len(odda)):
            ans+=abs(odda[y]-oddb[y])//2
        print(ans)
