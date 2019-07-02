N=int(input())
l1=[]
if 1<=N<=10000:
  for i in range(1,N+1):
    l1.append(i)
print(l1)
print(min(l1))