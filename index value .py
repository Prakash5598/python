num=int(input())
l1=list(map(int,input().split()))[:num]
a=len(l1)
l2=[]
i=0
while i<a:
  if i%2!=0 and l1[i]%2==0:
    l2.append(l1[i])
  elif i%2==0 and l1[i]%2!=0:
    l2.append(l1[i])
  i=i+1
print(*l2)
