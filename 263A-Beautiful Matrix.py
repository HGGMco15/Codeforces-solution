num1posy=0
num2posx=0
for x in range(5):
    a=list(map(int,input().split()))
    if 1 in a:
        num1posy=5-x
        num1posx=a.index(1)+1
cout=abs(num1posy-3)+abs(num1posx-3)
print(cout)
