t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cout=0
    while True:
        s=a.count(-1)
        if s%2==0 and sum(a)>=0:
            print(cout)
            break
        cout+=1
        a.remove(-1)
        a.append(1)
