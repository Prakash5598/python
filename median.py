#import math      #two methods to be solved 1) math fun and 2)normal method
n=int(input())
num=list(map(int,input().split()))[:n]
a=num.sort()
middleIndex =int( (len(num))/2)
#print(math.ceil(middleIndex))
print(num[middleIndex])