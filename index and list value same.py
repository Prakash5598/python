n=int(input())
l1=list(map(int,input().split()))[:n]
a=len(l1)
l2=[]
i=0
while i<a:
  if i==l1[i]:
    l2.append(i)
  i=i+1
if l2:
  print(*l2)
  
else:
  print("-1")
  
