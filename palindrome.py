get_number=int(input())
temp=get_number
palin=0
if get_number<=1000:
    while get_number!=0:
         digit=get_number%10
         palin=palin*10+digit
         get_number=get_number//10
    if temp==palin:
        print("yes")
    else:
        print("no")

    
