ini,end=map(int,input().split())
for num in range(ini+1,end):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
   if num == sum:
       print(num,end=' ')