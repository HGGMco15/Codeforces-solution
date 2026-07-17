t=int(input())
bestc=""
bestscore=-10000
for x in range(t):
    a=list(map(str,input().split()))
 
    sums=0
    for y in range(len(a)):
        if y==1 or y==2 and y!=0:
            if y==1:
                sums+=int(a[y])*100
            else:
                sums-=int(a[y])*50
        else:
            if y!=0:
                sums+=int(a[y])
    if sums>bestscore:
        bestscore=sums
        bestc=a[0]
print(bestc)
