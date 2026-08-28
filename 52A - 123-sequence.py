from collections import Counter
n=int(input())
a=list(map(int,input().split()))
d=Counter(a)
c=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
ls=[]
for c,val in c.items():
    ls.append(val)
print(len(a)-ls[0])
