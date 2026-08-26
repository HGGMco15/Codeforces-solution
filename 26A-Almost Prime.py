def check(m):
    if m<=1:
        return False
    if m<=3:
        return True
    if m%2==0 or m%3==0:
        return False
    i=5
    while i*i<=m:
        if m%i==0 or m%(i+2)==0:
            return False
        i+=6
    return True
n=int(input())
cout1=0
for x in range(1,n+1):
    cout=0
    for y in range(1,x+1):
        if check(y) and x%y==0:
            cout+=1
    if cout==2:
        cout1+=1
print(cout1)
