num=int(input())
l1=list(map(int,input().split()))[:num]
a=len(l1)
l2=[]
for i in range(a):
  k=i+1
  for j in range(k,a):
    if l1[i]==l1[j] and l1[i] not in l2:
      l2.append(l1[i])
l2.sort()
print(*l2,end=' ')