import sys
input=sys.stdin.readline
t=int(input())
for x in range(t):
    a=list(map(int,input().split()))
    cout=0
    for x in range(2):
        cout+=max(a)
        a.remove(max(a))
    if cout>=10:
        print("YES")
    else:
        print("NO")
