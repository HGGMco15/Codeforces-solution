t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mins=1e10
    maxs=-1000
    if n%2!=0:
        print("NO")
    else:
        for x in range(len(a)):
            if x%2==0:
                mins=min(a[x],mins)
            else:
                maxs=max(a[x],maxs)
        if maxs+1<mins:
            print("YES")
        else:
            print("NO")
