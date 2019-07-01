p,q=map(int,input().split())
n=list(map(int,input().split()))
num=0
for i in range(q):
  num=num+n[i]
print(num)
