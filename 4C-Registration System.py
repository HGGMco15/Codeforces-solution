from collections import defaultdict
t=int(input())
dtb=defaultdict(int) #using defaultdict to not get KeyError
for x in range(t):
    n=input()
    if n not in dtb:
        dtb[n]+=0
        print("OK")
    else:
        dtb[n]+=1
        print(f"{n}{dtb[n]}")
