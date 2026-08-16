t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if max(a)==min(a):
        print("NO")
    else:
        print("YES")
        print(a[len(a)-1],end=" ")
        print(*a[0:n-1])
