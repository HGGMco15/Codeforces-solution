n,k=map(int,input().split())
ls=[]
for x in range(n):
    p,t=map(int,input().split())
    ls.append((p,-t))
ls.sort(reverse=True)
# debug part:print(ls)
l=ls[k-1]
print(ls.count(l))
