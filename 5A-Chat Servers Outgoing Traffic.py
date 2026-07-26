import sys
#Using sys for reading the input
#Solution by HGGM (Rating:1000/Tags:Implementation)
executor=sys.stdin.read().splitlines()
person=0
byte=0
for l in executor:
    cout=0
    if l[0]=="+":
        person+=1
    elif l[0]=="-":
        person-=1
    else:
        for x in range(len(l)):
            if l[x]==":":
                cout+=1
                break
            else:
                cout+=1
        byte+=(len(l)-cout)*person 
print(byte)
