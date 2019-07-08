n=int(input())
num=list(map(int,input().split()))[:n]
a=len(num)
for i in range(a):
  print(num[i],end=" ")
  print(i)
  