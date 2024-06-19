l=list(map(int,input().split(" ")))
i=0
n=len(l)
for j in range(0,n):
  for i in range(0,n-1-j):
    if l[i]>l[i+1]:
      l[i],l[i+1]=l[i+1],l[i]
    else:
      i+=1
print(l)        
