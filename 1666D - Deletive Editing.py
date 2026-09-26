from collections import Counter,defaultdict
t=int(input())
for x in range(t):
    s,t=map(str,input().split())
    for y in t:
        if y not in s:
            print("NO")
            break
    else:
        f=set(t)
        for y in f:
            if t.count(y)>s.count(y):
                print("NO")
                break
        else:
            d=Counter(t)
            e=defaultdict(set)
            for i,cout in d.items():
                hi=len(s)-1
                a=cout
                while a>0:
                    if s[hi]==i:
                        e[i].add(hi)
                        a-=1
                    hi-=1
            ls=[]
            for i,cout in e.items():
                for y in cout:
                    ls.append(y)
            ls.sort()
            st=""
            for y in ls:
                st+=s[y]
            if st==t:
                print("YES")
            else:
                print("NO")
