t=int(input())
for x in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if k in a: #just have to check wheter k is in the array or not
        print("YES")
    else:
        print("NO")
