t=int(input())
for x in range(t):
    n,k=map(int,input().split())
    if n%k==0:
        print("YES")
    else:
        c=n-k 
        if c%2==0:
            print("YES")
        else:
            if n%2==0:
                print("YES")
            else:
                print("NO")
