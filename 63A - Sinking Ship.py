t=int(input())
ls=[]
ls2=[]
fin=[]
for x in range(t):
    s,prior=map(str,input().split())
    ls.append(s)
    ls2.append(prior)
for x in range(4):
    for y in range(len(ls)):
        if x==0:
            if ls2[y]=="rat":
                fin.append(ls[y])
        if x==1:
            if ls2[y]=="woman" or ls2[y]=="child":
                fin.append(ls[y])
        if x==2:
            if ls2[y]=="man":
                fin.append(ls[y])
        if x==3:
            if ls2[y]=="captain":
                fin.append(ls[y])
for p in fin:
    print(p)
