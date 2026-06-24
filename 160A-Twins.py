n=int(input())
a=list(map(int,input().split()))
x=0
you=0
twin=0
c=sorted(a,reverse=True)
while True:
    you+=c[x]
    twin=sum(c)-you
    x+=1
    if you>twin:
        print(x)
        break
