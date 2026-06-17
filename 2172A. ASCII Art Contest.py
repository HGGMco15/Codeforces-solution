g,c,l=map(int,input().split())
diff=max(g,c,l)-min(g,c,l)

if diff>=10:
    print("check again")
else:
    print("final",min(max(g,c),l))
