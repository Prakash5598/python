n=int(input())
l1=list(map(int,input().split()))[:n]
l1.sort()
print(*l1, sep = ' ')

