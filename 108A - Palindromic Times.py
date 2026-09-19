def pl(d):
    return d==d[::-1]
s=input()
hh=""
mm=""
past=False
for x in s:
    if x==":":
        past=True
    else:
        if past:
            mm+=x 
        else:
            hh+=x
minu=int(mm)
hour=int(hh)
while True:
    minu+=1
    if minu==60:
        minu=0
        hour+=1
    if hour==24:
        hour=0
    string=f"{str(hour).zfill(2)}:{str(minu).zfill(2)}"
    if pl(string):
        break 
print(f"{str(hour).zfill(2)}:{str(minu).zfill(2)}")
