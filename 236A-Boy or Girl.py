s=str(input())
ls=[]
for x in range(len(s)):
    if s[x] not in ls:
        ls.append(s[x])

if len(ls)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
