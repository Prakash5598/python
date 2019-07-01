N,Q=map(int,input().split())
if N<=10000 and Q<=10000:
     for i in range(N+1,Q):
         if i%2==0:
           print(i)
      
