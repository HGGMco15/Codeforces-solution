from collections import Counter
n=int(input())
a=list(map(int,input().split()))
c=len(set(a))
b=Counter(a)
d=dict(sorted(b.items(),key=lambda item:item[1]))
ls=[]
for i,cout in d.items():
    ls.append(cout)
print(ls[len(ls)-1],c)
