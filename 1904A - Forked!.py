import sys
input=sys.stdin.readline
t=int(input())
for x in range(t):
    a,b=map(int,input().split())
    kx,ky=map(int,input().split())
    qx,qy=map(int,input().split())
    ost=[(a,b),(-a,b),(a,-b),(-a,-b)]
    kpos=set()
    qpos=set()
    for dx,dy in ost:
        kpos.add((kx+dx,ky+dy))
        kpos.add((kx+dy,ky+dx))
        qpos.add((qx+dx,qy+dy))
        qpos.add((qx+dy,qy+dx))
    cout=0
    for x in kpos:
        if x in qpos:
            cout+=1
    print(cout)
