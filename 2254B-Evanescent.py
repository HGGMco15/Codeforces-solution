t=int(input())
for x in range(t):
    n=int(input())
    a=input()
    L=1
    for i in range(1,n):
        if a[i]!=a[i-1]:
            L+=1
    lb=False
    diff=False
    for i in range(1,n-1):
        if a[i-1]==a[i+1] and a[i]!=a[i-1]:
            lb=True
            break
        if a[i]!=a[i-1] and a[i]!=a[i+1]:
            diff=True
    if lb:
        print(L-2)
    elif diff:
        print(L-1)
    else:
        print(L)
