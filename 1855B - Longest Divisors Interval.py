import sys
input=sys.stdin.readline
t=int(input())
for x in range(t):
    n=int(input())
    i=1
    while n%i==0:
        i+=1
    print(i-1)
