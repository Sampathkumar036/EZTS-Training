li=[2,4,3,5,6,3,4,6,7,1,2,5]
max=0
sum=0
k=int(input("enter the continuous number digit:"))
for i in range(0,len(li)-k-1):
  sum=0
  for j in range(0,k):
    sum+=li[i+j]
  if sum>max:
    max=sum
    pos=i
print(max)
for j in range(0,k):
  print(li[pos+j])    
