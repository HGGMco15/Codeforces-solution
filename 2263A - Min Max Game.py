t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if a.count(1)>=a.count(0):
        print("Bessie")
    else:
        print("Elsie")
