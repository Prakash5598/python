word=str(input())
a=list(word)
count=0
for i in a:
  if i.isnumeric()==True:
    count=count+1
print(count)