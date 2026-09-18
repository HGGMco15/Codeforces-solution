n,m,c=list(map(str,input().split()))
n=int(n)
m=int(m)
room=[]
for x in range(n):
    s=input()
    ls=[]
    for y in s:
        ls.append(y)
    room.append(ls)
cout=0
dep=set()
for i in range(len(room)):
    for j in range(len(room[i])):
        d=room[i][j]
        if d==c:
            if i==0:
                if j==0:
                    if j+1<len(room[i]) and room[i][j+1]!=c and room[i][j+1]!=".":
                        dep.add(room[i][j+1])
                    if i+1<len(room) and room[i+1][j]!=c and room[i+1][j]!=".":
                        dep.add(room[i+1][j])
                elif j==len(room[i])-1:
                    if j-1>=0 and room[i][j-1]!=c and room[i][j-1]!=".":
                        dep.add(room[i][j-1])
                    if i+1<len(room) and room[i+1][j]!=c and room[i+1][j]!=".":
                        dep.add(room[i+1][j])
                else:
                    if j-1>=0 and room[i][j-1]!=c and room[i][j-1]!=".":
                        dep.add(room[i][j-1])
                    if j+1<len(room[i]) and room[i][j+1]!=c and room[i][j+1]!=".":
                        dep.add(room[i][j+1])
                    if i+1<len(room) and room[i+1][j]!=c and room[i+1][j]!=".":
                        dep.add(room[i+1][j])
            elif i==len(room)-1:
                if j==0:
                    if j+1<len(room[i]) and room[i][j+1]!=c and room[i][j+1]!=".":
                        dep.add(room[i][j+1])
                    if i-1>=0 and room[i-1][j]!=c and room[i-1][j]!=".":
                        dep.add(room[i-1][j])
                elif j==len(room[i])-1:
                    if j-1>=0 and room[i][j-1]!=c and room[i][j-1]!=".":
                        dep.add(room[i][j-1])
                    if i-1>=0 and room[i-1][j]!=c and room[i-1][j]!=".":
                        dep.add(room[i-1][j])
                else:
                    if j-1>=0 and room[i][j-1]!=c and room[i][j-1]!=".":
                        dep.add(room[i][j-1])
                    if j+1<len(room[i]) and room[i][j+1]!=c and room[i][j+1]!=".":
                        dep.add(room[i][j+1])
                    if i-1>=0 and room[i-1][j]!=c and room[i-1][j]!=".":
                        dep.add(room[i-1][j])
            else:
                if j==0:
                    if j+1<len(room[i]) and room[i][j+1]!=c and room[i][j+1]!=".":
                        dep.add(room[i][j+1])
                    if i-1>=0 and room[i-1][j]!=c and room[i-1][j]!=".":
                        dep.add(room[i-1][j])
                    if i+1<len(room) and room[i+1][j]!=c and room[i+1][j]!=".":
                        dep.add(room[i+1][j])
                        cout+=1
                elif j==len(room[i])-1:
                    if j-1>=0 and room[i][j-1]!=c and room[i][j-1]!=".":
                        dep.add(room[i][j-1])
                    if i-1>=0 and room[i-1][j]!=c and room[i-1][j]!=".":
                        dep.add(room[i-1][j])
                    if i+1<len(room) and room[i+1][j]!=c and room[i+1][j]!=".":
                        dep.add(room[i+1][j])
                        cout+=1
                else: 
                    if j-1>=0 and room[i][j-1]!=c and room[i][j-1]!=".":
                        dep.add(room[i][j-1])
                    if j+1<len(room[i]) and room[i][j+1]!=c and room[i][j+1]!=".":
                        dep.add(room[i][j+1])
                    if i-1>=0 and room[i-1][j]!=c and room[i-1][j]!=".":
                        dep.add(room[i-1][j])
                    if i+1<len(room) and room[i+1][j]!=c and room[i+1][j]!=".":
                        dep.add(room[i+1][j])
print(len(dep))
