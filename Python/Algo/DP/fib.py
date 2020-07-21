import time


# By Recursion

def recursion(n):
	if n == 0 or n == 1:
		return n
	return recursion(n - 1) + recursion(n - 2)


# By Dp (Top Down)


def topDownDp(n, dp):
	if n == 0 or n == 1:
		dp[n] = n

	if dp[n] != -1:
		return dp[n]

	else:

		dp[n] = topDownDp(n - 1, dp) + topDownDp(n - 2, dp)
		return dp[n]


# By Dp (Bottom Up)

def bottomUp(n):
	start = time.time()
	if n == 0 or n == 1:
		return n
	dp = [-1] * (n + 1)
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n + 1):
		dp[i] = dp[i - 1] + dp[i - 2]

	stop = time.time() - start
	print("Bottom Up= ", *dp)
	print("Time = ", stop)
	print()


n = int(input("Enter number of elements= "))
dp = [-1] * (n + 1)

start = time.time()

topDownDp(n, dp)

stop = time.time() - start
print("Top Down = ", *dp)
print("Time = ", stop)
print()

bottomUp(n)

start = time.time()
print("Recursion = ", recursion(n))
stop = time.time() - start

print("Time = ", stop)
print()
