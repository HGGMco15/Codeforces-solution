import sys
input=sys.stdin.readline
t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cs=max(a)+1
    b=[]
    for l in a:
        b.append(cs-l)
    print(*b)
