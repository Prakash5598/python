num=int(input())
amst=0
count=0
class number_count:
    while num!=0:
        digit=num%10
        count=count+1
        num=num//10
class cal:
    ob=number_count
    while num!=0:
        digit1=num%10
        amst=amst+digit1**ob.count
        num=num//10
ob1=cal
if ob1.amst==num:
    print("yes")
else:
    print("no")
