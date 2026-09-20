n=int(input())
a=list(map(int,input().split()))
maxflown=1
lo=0
hi=0
for x in range(len(a)):
    prevlo=x 
    prevhi=x
    cout=1 
    lo=x-1
    hi=x+1
    while lo>=0:
        if a[lo]<=a[prevlo]:
            cout+=1
            prevlo-=1
            lo-=1
        else:
            break
    while hi<len(a):
        if a[hi]<=a[prevhi]:
            cout+=1
            prevhi+=1
            hi+=1
        else:
            break
    maxflown=max(maxflown,cout)
print(maxflown)
