n=int(input())
a=list(map(int,input().split()))
 
a.sort()
for p in a:
    print(p,end=" ")
