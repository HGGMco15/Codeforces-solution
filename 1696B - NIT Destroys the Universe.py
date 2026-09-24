t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cout=0
    ls=[]
    for y in a:
        if y!=0:
            ls.append(y)
        else:
            if ls:
                cout+=1
                ls=[]
    if ls:
        cout+=1
        ls=[]
    if cout>=2:
        print(2)
    else:
        print(cout)
