m=input()
n=int(input())
mls=[
    "January","February","March","April", 
    "May","June","July","August", 
    "September","October","November","December"
]
if n%12==0:
    print(m)
else:
    n-=12-mls.index(m)
    print(mls[n%12])
