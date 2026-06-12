n=int(input())
ls=[]
for x in range(n):
    sum1=0
    sum2=0
    char=[]
    a=str(input())
    for y in range(len(a)):
        char.append(a[y])
    for m in range(0,3):
        sum1+=int(char[m])
    for u in range(3,6):
        sum2+=int(char[u])
    if sum1==sum2:
        ls.append("YES")
    else:
        ls.append("NO")
 
for p in ls:
    print(p)
