import math
t=int(input())
for x in range(t):
    n=int(input())
    fd=n//pow(10,int(math.log10(n)))
    cout=int(math.log10(n))+1
    ans=(9*(cout-1)+fd)
    print(ans)
