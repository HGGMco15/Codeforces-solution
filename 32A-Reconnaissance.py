n,d=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
cout=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[j]<a[i] or a[j]>a[i] or (a[i]==a[j] and i!=j) :
            if a[i]-a[j]<=d and a[i]-a[j]>0:
                cout+=1
            elif a[i]==a[j]:
                cout+=1
            else:
                if a[j]-a[i]<=d and a[j]-a[i]>0:
                    cout+=1
print(cout)
