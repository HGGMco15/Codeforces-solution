t=int(input())
for c in range(t):
    x=0
    posx=[]
    posy=[]
    for l in range(10):
        x+=1
        a=input()
        for k in range(len(a)):
            if a[k]=="X":
                posx.append(k+1)
                posy.append(x)
    cout=0
    for v in range(len(posx)):
        if posy[v]==1 or posy[v]==10:
            cout+=1
        elif posy[v]==2 or posy[v]==9:
            if posx[v]==1 or posx[v]==10:
                cout+=1
            else:
                cout+=2
        elif posy[v]==3 or posy[v]==8:
            if posx[v]==1 or posx[v]==10:
                cout+=1
            elif posx[v]==2 or posx[v]==9:
                cout+=2
            else:
                cout+=3
        elif posy[v]==4 or posy[v]==7:
            if posx[v]==1 or posx[v]==10:
                cout+=1
            elif posx[v]==2 or posx[v]==9:
                cout+=2
            elif posx[v]==3 or posx[v]==8:
                cout+=3
            else:
                cout+=4
        else:
            if posx[v]==1 or posx[v]==10:
                cout+=1
            elif posx[v]==2 or posx[v]==9:
                cout+=2
            elif posx[v]==3 or posx[v]==8:
                cout+=3
            elif posx[v]==4 or posx[v]==7:
                cout+=4
            else:
                cout+=5
    print(cout)
