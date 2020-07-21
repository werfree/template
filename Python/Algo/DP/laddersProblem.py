"""
    On can take max of k jump (i.e 1,2,3, ...,k jump).
    Find no of ways to reach n.
"""

#Recursion

def recursion(n):
    if(n == 0):
        return 1
    if n < 0:
        return 0
    ans = recursion(n-1) + recursion(n-2) + recursion(n-3)
    return (ans)


# By Dp (Bottom Up)

def buttomUp (n,k):
    if 0 <= n <= k:
        return n
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(1, k+1):
            if i-j < 0:
                break
            else:
                dp[i] = dp[i]+dp[i-j]

    print(dp[n])


n = int(input("Enter number of ladder = "))
k = int(input("Max Jump one can take = "))
buttomUp(n, k)
print(recursion(n))
