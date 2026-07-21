x,y=map(int,input().split())
def check(s):
    if s<2:
        return False
    else:
        cout=0
        i=1
        while i*i<=s:
            if s%i==0:
                cout+=1
                if i!=s//i:
                    cout+=1
            i+=1
        if cout<=2:
            return True
        else:
            return False
if check(y):
    for l in range(x+1,y+1):
        if check(l) and l!=y:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")
