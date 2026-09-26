t=int(input())
for x in range(t):
    n=int(input())
    if n%2!=0 or n<4:
        print(-1)
    else:
        if n%6==0:
            mn=n//6
        else:
            mn=n//6+1
        print(mn,n//4)
