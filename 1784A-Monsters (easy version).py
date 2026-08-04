t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ls=sorted(a)
    cout=0
    tar=1
    for y in range(len(ls)):
        if ls[y]>=tar:
            cout+=ls[y]-tar
            tar+=1
    print(cout)
