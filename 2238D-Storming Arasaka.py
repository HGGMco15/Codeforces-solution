t=int(input())
ans=[]
 
for _ in range(t):
 
 n=int(input())
 sums=0
 kinds=0
 
 x=2
 
 while x*x<=n:
 
  cout=0
 
  while n%x==0:
   cout+=1
   n//=x
 
  if cout:
   sums+=cout
   kinds+=1
 
  x+=1
 
 if n>1:
  sums+=1
  kinds+=1
 
 ans.append(sums+kinds-1)
 
for x in ans:
 print(x)
