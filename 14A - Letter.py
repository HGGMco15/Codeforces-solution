n,m=map(int,input().split())
ls=[]
lo=1e9
hi=-1e9
for x in range(n):
    s=input()
    if "*" in s:
        lo=min(s.find("*"),lo)
        hi=max(s.rfind("*"),hi)
    ls.append(s)
for lols in range(len(ls)):
    if "*" in ls[lols]:
        break 
for hils in range(len(ls)-1,0-1,-1):
    if "*" in ls[hils]:
        break 
d=ls[lols:hils+1]
for x in d:
    print(x[lo:hi+1])
