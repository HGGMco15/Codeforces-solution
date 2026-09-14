a=input()
b=input()
c=int(a)+int(b)
newb=""
newa=""
newc=""
for x in range(len(str(a))):
    if a[x]!="0":
        newa+=a[x]
for x in range(len(str(b))):
    if b[x]!="0":
        newb+=b[x]
for x in range(len(str(c))):
    if str(c)[x]!="0":
        newc+=str(c)[x]
if (int(newa)+int(newb)==int(newc)):
    print("YES")
else:
    print("NO")
