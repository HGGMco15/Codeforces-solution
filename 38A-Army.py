n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
a-=1
b-=1
cout=0
for m in range(len(d)):
    if m>=a and m<b:
        cout+=d[m]
print(cout)
