import sys
import math
input=sys.stdin.readline
t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))!=1:
        if a.count(2)%2!=0:
            print(-1)
        else:
            #AI debug 
            pref = [0] * (n + 1)
            for i in range(n):
                pref[i+1] = pref[i] + (1 if a[i] == 2 else 0)

            for y in range(len(a)):
                if y==0:
                    left_twos = pref[y+1] - pref[0]
                    right_twos = pref[n] - pref[y+1]
                    if left_twos == right_twos:
                        print(y+1)
                        break
                else:
                    left_twos = pref[y] - pref[0]
                    right_twos = pref[n] - pref[y]
                    if left_twos == right_twos:
                        print(y)
                        break
            else:
                print(-1)
            #for y in range(len(a)):
                #if len(a[0:y])==0:
                    #if math.prod(a[0:y+1])==math.prod(a[y+1:n]):
                        #print(y+1)
                        #break
                #else:
                    #if math.prod(a[0:y])==math.prod(a[y:n]):
                        #print(y)
                        #break
            #else:
                #print(-1)  (Original code)
    else:
        if 1 in a:
            print(1)
        else:
            if len(a)%2==0:
                print(n//2)
            else:
                print(-1)
