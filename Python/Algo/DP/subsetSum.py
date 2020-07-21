t = int(input())

def isSubsetSumPresent(a,s,n):
  dp = [[-1]*(s+1)for i in range(n+1)]

  for i in range(n+1):
    for j in range(s+1):
      if(i==0 or j==0):
        dp[i][j]=0
        continue
      if a[i-1]==j:
        dp[i][j] = 1
      elif a[i-1]<j:
        dp[i][j] = dp[i-1][j]+dp[i-1][j-a[i-1]]
      else:
        dp[i][j] = dp[i-1][j]
  return dp
        
  
while t:
  n = int(input())
  a = list(map(int,input().split()))
  found = False
  S = sum(a)
  if S%2:
    print("1 NO")
  else:
    S = S//2
    dp = isSubsetSumPresent(a,S,n)
    for i in range(n+1):
      if dp[i][S]!=0:
        print("YES")
        found =True
        break
    if(not found):
      print("NO")
  t-=1
