n=int(input())
a=list(map(int,input().split()))
for x in range(len(a)):
    a[x]=abs(a[x])
if 0 in a:
    print(0)
else:
    print(min(a))
