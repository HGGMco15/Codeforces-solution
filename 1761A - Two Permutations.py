t=int(input())
for x in range(t):
    n,a,b=map(int,input().split())
    if a==n and b==n:
        print("YES")
    else:
        if n-(a+b)>=2:
            print("YES")
        else:
            print("NO")
