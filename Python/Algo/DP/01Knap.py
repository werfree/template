
t = int(input())

def go( val, w, W, n):
  global dp

  if W == 0 or n==0:
    return 0

  if dp[n][W]!= []:
    return  dp[n][W]
  i = j =0
  if w[n-1] <= W:
    i= max(val[n-1] + go(
       val, w, W - w[n-1], n - 1),go(
     val, w, W, n - 1))
  else:
      j =  go(
         val, w, W, n - 1)
  dp[n][W] = max(i,j)
  return dp[n][W]
while t:
    n = int(input())
    W = int(input())
    val = list(map(int,input().split()))
    wt = list(map(int,input().split()))
    dp = [[-1 for i in range(W+1)]for j in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            
            if i==0 or j==0:
                dp[i][j]=0
            elif wt[i-1]<=j:
              dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            
            else:
                dp[i][j] = dp[i-1][j]
    
               
    print(dp[n][W])
    dp = [[-1 for i in range(W+1)]for j in range(n+1)]
    print(go(val, wt, W,n))
   
    t-=1
