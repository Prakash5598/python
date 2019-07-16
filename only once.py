num=list(map(int,input().split()))
a=len(num)
for i in range (a):
   if num.count(i)==1:
    print(i)
