def merge(l,low,mid,high):
  
 
  temp=[0]*len(l)
  i=j=t=0

  while i<left(left) and j<len(right):
    if left[i]<right[j]:
      temp[t]=left[i]
      i+=1
      t+=1
    else:
      temp[t]=right[j]
      j+=1
      t+=1

  while i<len(left) :
    temp[t]=left[i]
    i+=1
    t+=1
  while i<len(right) : 
    temp[t]=right[j]
    i+=1
    t+=1

def mergesort(l,low,high):
  if low<high:
    mid=low + (high-low)//2
    mergesort(l,low,mid)
    mergesort(l,mid+1,high)
    merge(l,low,mid,high)
if __name__=="__main__":
  l=list(map(int,input().split()))
  merge(l,0,len(l)-1)

  print("sorted array=",l)

