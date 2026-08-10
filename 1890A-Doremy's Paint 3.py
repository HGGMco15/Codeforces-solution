from collections import Counter
t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))>2:
        print("NO")
    else:
        d=Counter(a)
        c=dict(sorted(d.items(),key=lambda item:item[1]))
        prev=next(iter(c.values()))
        for i,cout in c.items():
            if cout==prev or cout-1==prev:
                prev=cout
            else:
                print("NO")
                break
        else:
            print("YES")
