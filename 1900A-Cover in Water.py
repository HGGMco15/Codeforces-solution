t=int(input())
for x in range(t):
    n=int(input())
    a=list(input())
    cout3=0
    coutd=0
    if a.count(".")==0:
        print(0)
    else:
        if n==3 or n==2:
            couth=0
            coutd=0
            for c in range(n):
                if a[c]=="#":
                    couth+=1
                elif a[c]==".":
                    coutd+=1
            if n==2:
                print(coutd)
            else:
                if coutd==3:
                    print(2)
                else:
                    print(coutd)
        elif n==1:
            print(1)
        else:
            for c in range(n):
                if a[c]==".":
                    coutd+=1
            for l in range(1,n-1):
                if a[l-1]==a[l]==a[l+1]==".":
                    cout3+=1
            if cout3>0:
                print(2)
            else:
                print(coutd)
