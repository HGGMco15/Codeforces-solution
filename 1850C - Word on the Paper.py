import sys
input=sys.stdin.readline
t=int(input())
for x in range(t):
    st=""
    for y in range(8):
        s=list(input())
        for i in s:
            if i.isalpha():
                st=st+i
    print(st)
