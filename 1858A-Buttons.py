t=int(input())
for x in range(t):
    a,b,c=map(int,input().split())
    if a>b or a<b:
        if a>b:
            print("First")
        else:
            print("Second")
    else:
        if c%2==0:
            print("Second")
        else:
            print("First")
