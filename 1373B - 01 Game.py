t=int(input())
for x in range(t):
    n=list(input())
    if n.count("1")==0 or n.count("0")==0:
        print("NET")
    else:
        if min(n.count("1"),n.count("0"))%2==0:
            print("NET")
        else:
            print("DA")
