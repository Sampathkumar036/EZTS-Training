ls=[[1,2,2,3],[3,1,4,2],[1,5,3,3],[1,2,1,1]]
n=len(ls)-1
m=len(ls[0])-1

i=0
j=0
sum=m[i][j]
while i<n and j<m:
  if i==n:
    j+=1
  elif j==m:
    i=i+1
  elif m[i][j+1] < m[i+1][j]:
    j+=1
  else:
    i+=1
  sum+=m[i][j]    

print(sum)