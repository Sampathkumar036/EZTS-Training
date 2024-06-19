li=[2,4,3,5,6,3,4,6,7,1,2,5]
max=0
window=0
k=int(input("enter the continuous number digit:"))
for j in range(0,k):
    window+=li[j]


for i in range(0,len(li)-k):
  if max<window:
     max=window
     pos=i
     
  window=window+li[i+k]-li[i] 
print(max)
for j in range(0,k):
  print(li[pos+j])
    