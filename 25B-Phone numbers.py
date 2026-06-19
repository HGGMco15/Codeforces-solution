n=int(input())
s=str(input())
ls=[]
for y in s:
    ls.append(y)

cout=2
for x in range(int(n/2)-1):
    ls.insert(cout,"-")
    cout+=3
for p in ls:
    print(p,end="")
