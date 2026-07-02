import math

t = int(input())
ans = []

for _ in range(t):
    n, d = map(int, input().split())
    if d <= n:
        ans.append("YES")
    else:
        y = int(math.sqrt(d)) - 1
        opt1 = y + math.ceil(d / (y + 1))
        opt2 = (y + 1) + math.ceil(d / (y + 2))
        
        if min(opt1, opt2) <= n:
            ans.append("YES")
        else:
            ans.append("NO")

for p in ans:
    print(p)
