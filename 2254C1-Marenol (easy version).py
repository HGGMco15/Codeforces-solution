t=int(input())
for x in range(t):
    n=int(input())
    a=input()
    b=input()
    if n<3 and a!=b:
        print("NO")
    else:
        if a==b:
            print("YES")
        else:
            odda=0
            oddb=0
            eva=0
            evb=0
            for x in range(len(a)):
                if x%2==0 and a[x]=="1":
                    eva+=1
                else:
                    if a[x]=="1":
                        odda+=1
            for x in range(len(b)):
                if x%2==0 and b[x]=="1":
                    evb+=1
                else:
                    if b[x]=="1":
                        oddb+=1
            if eva==evb and odda==oddb:
                print("YES")
            else:
                print("NO")
