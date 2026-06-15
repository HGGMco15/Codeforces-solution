s=str(input())
ls=[]
count=0
for x in range(len(s)):
    if s[x]!="+":
        ls.append(s[x])
    else:
        count+=1
ls.sort()
if count==0:
    print(s)
else:
    ind=1
    for c in range(count):
        ls.insert(ind,"+")
        ind+=2
    print("".join(ls))
    
