t=int(input())
count=0
for x in range(t):
    a,b=map(int,input().split())
    if b-a>=2:
        count+=1

print(count)
