n=int(input())
num=list(map(int,input().split()))[:n]
for i in range (len(num)):
   if num.count(i)==1:
    print(i)
