n=int(input())
s=0
 
for x in range(n):
    a=str(input())
    if a=="X++" or a=="++X":
        s+=1 
    else:
        s-=1 
print(s)
