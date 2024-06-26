def calc_max(p,w,c,n,dp):
  if n==0 or c==0:
    return 0
  for i in range(1,len(p)+1):
    for c in range(1,c+1):
      dp[i][c]=max(dp[i-1][c],p[i-1]+dp[i-1][c-w[i-1]])
    return dp


p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
c=15
n=len(w)
dp=[[0 for i in range(c+1)] for j in range(n+1)]
print(calc_max(p,w,c,dp,n))