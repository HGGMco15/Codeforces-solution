n=int(input())
n+=1
def check(m):
    ls=[]
    for x in range(len(m)):
        if m[x] not in ls:
            ls.append(m[x])
    if len(ls)==len(m):
        return True
    else:
        return False
 
while True:
    if check(str(n)):
        print(n)
        break
    else:
        n+=1
