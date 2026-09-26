t=int(input())
for x in range(t):
    n=input()
    step00=0
    step25=0
    step50=0
    step75=0
    st=""
    for y in n:
        if y=="0":
            st+=y
    if "00" not in st:
        step00=1e18
    st=""
    for y in n:
        if y=="2" or y=="5":
            st+=y
    if "25" not in st:
        step25=1e18
    st=""
    for y in n:
        if y=="5" or y=="0":
            st+=y
    if "50" not in st:
        step50=1e18
    st=""
    for y in n:
        if y=="7" or y=="5":
            st+=y
    if "75" not in st:
        step75=1e18
    if step00!=1e18:
        lo=len(n)-1
        while n[lo]!="0":
            step00+=1
            lo-=1
        lo-=1
        while n[lo]!="0":
            step00+=1
            lo-=1
    if step25!=1e18:
        lo=len(n)-1
        while n[lo]!="5":
            step25+=1
            lo-=1
        lo-=1
        while n[lo]!="2":
            step25+=1
            lo-=1
    if step50!=1e18:
        lo=len(n)-1
        while n[lo]!="0":
            step50+=1
            lo-=1
        lo-=1
        while n[lo]!="5":
            step50+=1
            lo-=1
    if step75!=1e18:
        lo=len(n)-1
        while n[lo]!="5":
            step75+=1
            lo-=1
        lo-=1
        while n[lo]!="7":
            step75+=1
            lo-=1
    if min(step00,step25,step50,step75)==1e18:
        print(-1)
    else:
        print(min(step00,step25,step50,step75))
