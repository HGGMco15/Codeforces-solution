t=int(input())
for x in range(t):
    n,k=map(int,input().split())
    m=n-1-k
    blks=m+1
    found=False
    for start in "01":
        if found:
            break
        if blks%2==0:
            c0=blks//2
            c1=blks//2
        else:
            if start=="0":
                c0=(blks+1)//2
                c1=(blks-1)//2
            else:
                c0=(blks-1)//2
                c1=(blks+1)//2
        for cnt0 in {n//2,(n+1)//2}:
            cnt1=n-cnt0
            if abs(cnt0-cnt1)<=1 and cnt0>=c0 and cnt1>=c1:
                if (c0==0 and cnt0>0) or (c1==0 and cnt1>0):
                    continue
                leng0=[1]*c0
                leng1=[1]*c1
                if c0>0:
                    leng0[0]+=cnt0-c0
                if c1>0:
                    leng1[0]+=cnt1-c1
                fin=[]
                i0=0
                i1=0
                cur=start
                for i in range(blks):
                    if cur=="0":
                        fin.append("0"*leng0[i0])
                        i0+=1
                        cur="1"
                    else:
                        fin.append("1"*leng1[i1])
                        i1+=1
                        cur="0"
                print("".join(fin))
                found=True
                break
    if not found:
        print(-1)
