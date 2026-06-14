n = int(input())
 
div_count = [0] * (n + 1)
 
for p in range(2, n + 1):
    if div_count[p] == 0:
        for multiple in range(p, n + 1, p):
            div_count[multiple] += 1
 
count = 0
for i in range(2, n + 1):
    if div_count[i] == 2:
        count += 1
 
print(count)
