t = int(input())

def printDp(dp):
    for i in range(len(dp)):
        print(dp[i])
def lcs(x,y,n,m,dp):
    if n==0 or m==0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
  
    if (x[n-1] == y[m-1]):
        dp[n][m] = 1+lcs(x,y,n-1,m-1,dp)
    else:
        dp[n][m] = max(lcs(x,y,n-1,m,dp),lcs(x,y,n,m-1,dp))
    return dp[n][m]
while t:
    n = list(map(int, input().split()))
    m = n[1]
    n = n[0]
    x = (input())
    y = (input())
    dp = [[-1]*(m+1)for i in range(n+1)]
    
    #print(lcs(x,y,n,m,dp))
    dp = [[-1]*(m+1)for i in range(n+1)]
    result = ""
    k = -5
    
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j] = 0
                continue
            
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j]>k:
                    print(x[i-1])
                    result += x[i-1]
                    k = dp[i][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
               
                
   
    print(dp[n][m],result)
    t=t-1
