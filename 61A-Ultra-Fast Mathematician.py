a=str(input())
b=str(input())
sr=""
for i in range(len(a)):
    if a[i]==b[i]:
        sr=sr+"0"
    else:
        sr=sr+"1"
print(sr)
