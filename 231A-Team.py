n=int(input())
s=0
for x in range(n):
    ls=list(map(int,input().split()))
    a=ls.count(1)
    if a>=2:
        s+=1 
 
print(s)
