s=str(input()).lower()
vowl=["a","i","u","e","o","y"] #y is the semi-vowel btw
ls=[]
for x in range(len(s)):
    if s[x] not in vowl:
        ls.append(s[x])
if ls:
    print("."+".".join(ls))
else:
    print("")
