n := File standardInput readLine asNumber

if(n == 0 or n == 1,
    1 println
    System exit
)

f1 := 1
f2 := 1
for(i, 2, n,
    f := f1 + f2
    f1 = f2
    f2 = f
)

f2 println
