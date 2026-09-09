t=int(input())
for x in range(t):
    n,k=map(int,input().split())
    f=list(input())
    d=n//k
    cout=0
    for y in range(n):
        if y%k==0:
            c=f[y:y+k]
            if "0" not in c:
                cout+=1
    print(cout)
