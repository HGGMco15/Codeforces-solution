import sys
input=sys.stdin.readline
t=int(input())
def solve(tar,m,k):
    mn=(k*(k+1))//2
    mx=(k*(2*m-k+1))//2
    if tar<mn or tar>mx or k>m:
        return False
    else:
        te=[]
        for i in range(min(tar,m),0,-1):
            re=k-1
            mnre=(re*(re+1))//2
            mxre=(re*(2*(i-1)-re+1))//2
            if tar>=i and mnre<=(tar-i)<=mxre:
                te.append(i)
                tar-=i
                k-=1
            if k==0:
                break
        if tar==0 and k==0:
            return True
        else:
            return False
for d in range(t):
    n,k,x=map(int,input().split())
    mn=(k*(k+1))//2
    mx=(k*(2*n-k+1))//2
    if k<=n and mn<=x<=mx:
        print("YES")
    else:
        print("NO")
