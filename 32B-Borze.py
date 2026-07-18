s=str(input())
sr=""
ls=list(s)
i=0
while i<len(ls):
    if ls[i]==".":
        sr=sr+"0"
        i+=1
    else:
        if ls[i+1]==".":
            sr=sr+"1"
        else:
            sr=sr+"2"
        i+=2
print(sr)
