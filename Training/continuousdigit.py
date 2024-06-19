li=[2,4,3,5,6,3,4,6,7,1,2,5]
max=0
sum=0
for i in range(0,len(li)-2):
  sum=li[i]+li[i+1]+li[i+2]
  if sum>max:
    max=sum
    pos=i
print(max,li[pos],li[pos+1],li[pos+2])    