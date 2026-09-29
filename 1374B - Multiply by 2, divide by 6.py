from collections import Counter,defaultdict
import itertools
import math
import sys
input=sys.stdin.readline
t=int(input())
for x in range(t):
    n=int(input())
    cout=0
    while True:
        if n%6==0:
            n/=6
            cout+=1
        else:
            if n%3==0:
                n*=2
                cout+=1
            else:
                if n==1:
                    print(cout)
                    break
                else:
                    print(-1)
                    break
