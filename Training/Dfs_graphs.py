Al={
  1:[(1,2,0),(1,3,0)],
  2:[(2,1,0),(2,7,0)],
  3:[(3,1,0),(3,5,0),(3,6,0)],
  4:[(4,7,0),(4,8,0)],
  5:[(5,3,0),(5,7,0)],
  6:[(6,3,0),(6,8,0)],
  7:[(7,2,0),(7,4,0),(7,5,0)],
  8:[(8,4,0),(8,6,0)]
}
def dfs(Al,V,stack,ele):
  if V[ele]==False:
    stack.append(ele)
    V[ele]=True
  else:
    return
  print(stack.pop()) 
  for i in Al[ele]:
    dfs(Al,V,stack,i[1])

V={1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False}
stack=[]         
dfs(Al,V,stack,1)  
  