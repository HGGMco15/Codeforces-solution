s=input()
ls=[]
for x in range(10):
    n=input()
    ls.append(n)
x=0
pasw=""
while x<8:
    if x==0:
        c=s[0:10]
        pasw=pasw+str(ls.index(c))
    elif x==1:
        c=s[10:20]
        pasw=pasw+str(ls.index(c))
    elif x==2:
        c=s[20:30]
        pasw=pasw+str(ls.index(c))
    elif x==3:
        c=s[30:40]
        pasw=pasw+str(ls.index(c))
    elif x==4:
        c=s[40:50]
        pasw=pasw+str(ls.index(c))
    elif x==5:
        c=s[50:60]
        pasw=pasw+str(ls.index(c))
    elif x==6:
        c=s[60:70]
        pasw=pasw+str(ls.index(c))
    else:
        c=s[70:80]
        pasw=pasw+str(ls.index(c))
    x+=1
print(pasw)
