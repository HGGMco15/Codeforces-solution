n=int(input())
m=list(map(int,input().split()))
best=1
current=1
for x in range(1,len(m)):
    if m[x]>=m[x-1]:
        current+=1
        if best<=current:
            best=current
    else:
        current=1
print(best)
