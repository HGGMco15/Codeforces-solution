t=int(input())
ans=[]
for x in range(t):
    n=int(input())
    di=str(input())
    yaxis=0
    xaxis=0
    ls=[]
    for y in range(len(di)):
        if di[y]=="U":
            yaxis+=1
            ls.append((xaxis,yaxis))
        elif di[y]=="D":
            yaxis-=1
            ls.append((xaxis,yaxis))
        elif di[y]=="L":
            xaxis-=1
            ls.append((xaxis,yaxis))
        else:
            xaxis+=1
            ls.append((xaxis,yaxis))
    if (1,1) in ls:
        ans.append("YES")
    else:
        ans.append("NO")
for p in ans:
    print(p)
