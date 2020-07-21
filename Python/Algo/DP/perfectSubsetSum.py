t = int(input())


def printDP(a):
  for i in range(len(a)):
    print(a[i])
while t:

  n = int(input())
  a = list(map(int,input().split()))
  S = int(input())

  dp = [[0]*(S+1)for i in range(n+1)]

  s = 0

  for i in range(n+1):
    for j in range(S+1):
      if i==0 or j==0:    #We cannot get sum with array size 0
        dp[i][j] = 0
        continue
      '''
      if j==0:   #Sum can always be zero as empty subset 
        dp[i][j] = 1
        continue
      dp[0][0] = 1
      '''
    

      if(a[i-1]<j):
        dp[i][j] = (dp[i-1][j-a[i-1]]+dp[i-1][j])
      elif(a[i-1]==j ):
        dp[i][j] =  1+dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j]
  print(dp[n][S])
  #printDP(dp)
  
  
  t-=1
  
