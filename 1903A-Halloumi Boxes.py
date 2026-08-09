t=int(input())
def check():
    n=sorted(a)
    if n==a:
        return True
    return False
for x in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if check():
        print("YES")
    else:
        if k==1:
            print("NO")
        else:
            print("YES")
