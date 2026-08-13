import sys
input=sys.stdin.readline
t=int(input())
for c in range(t):
    x,k=map(int,input().split())
    if x<k:
        print(1)
        print(x)
    else:
        if x%k!=0:
            print(1)
            print(x)
        else:
            c=x
            while x%k==0:
                x-=1
            print(2)
            print(x,c-x)
