n=int(input())
a=list(map(int,input().split()))
def check():
    global a
    if a.count(1)>=1:
        print("HARD")
    else:
        print("EASY")
 
check()
