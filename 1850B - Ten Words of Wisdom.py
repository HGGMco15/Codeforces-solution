import sys
input=sys.stdin.readline
t=int(input())
for x in range(t):
    n=int(input())
    lenght=[]
    qal=[]
    for y in range(n):
        a,b=map(int,input().split())
        lenght.append(a)
        qal.append(b)
    bestqal=-1e9
    bestres=-1
    for i in range(len(lenght)):
        if lenght[i]<=10:
            if qal[i]>bestqal:
                bestqal=qal[i]
                bestres=i
    print(bestres+1)
