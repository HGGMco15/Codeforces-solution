n=input()
s=input()
s1=int(n)
s2=int(s)
ls=[]
if (len(str(n))!=len(str(s))):
    print("WRONG_ANSWER")
else:
    for x in range(len(str(s1))):
        ls.append(str(s1)[x])
    ls.sort()
    if ls[0]!="0":
        st=""
        for x in ls:
            st=st+x 
        if st==str(s2):
            print("OK")
        else:
            print("WRONG_ANSWER")
    else:
        if (s1==0 or s2==0):
            if (s1==s2):
                print("OK")
            else:
                print("WRONG_ANSWER")
        else:
            num0=0
            for x in range(len(ls)):
                if ls[x]=="0":
                    num0+=1
            for x in range(num0):
                ls.remove("0")
            mn=ls[0]
            hi=len(ls)-1
            while hi>=0:
                if ls[hi]==mn:
                    break
                hi-=1
            for y in range(num0):
                ls.insert(x+1,"0")
                st=""
            for x in ls:
                st=st+x
            if st==str(s2):
                print("OK")
            else:
                print("WRONG_ANSWER")
