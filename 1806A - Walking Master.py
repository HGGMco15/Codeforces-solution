t=int(input())
for x in range(t):
    a,b,c,d=map(int,input().split())
    if d>=b and a-b>=c-d:
        print((d-b)+((a+d-b)-c))
    else:
        print(-1)
