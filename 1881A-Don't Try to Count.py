import math
t=int(input())
for x in range(t):
    n,m=map(int,input().split())
    x=input()
    y=input()
    for i in range(6):
        if y in x:
            print(i)
            break
        x=x+x
    else:
        print(-1) 
