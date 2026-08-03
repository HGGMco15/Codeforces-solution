t=int(input())
cout1=0
cout2=0
ls=[]
ls1=[]
for x in range(t):
    s=input()
    if len(ls)==0 or s in ls:
        cout1+=1
        ls.append(s) #this might get MLE due to using too much space in the list,you can optimize it by checking the len of the list
    else:
        cout2+=1
        ls1.append(s)
if cout1>cout2:
    print(ls[0])
else:
    print(ls1[0])
