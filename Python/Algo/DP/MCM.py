
# ########## ------ Import ------- ##########

import sys
import math
from collections import Counter
from collections import deque as deq
from functools import lru_cache

# ########## ------ Define -------- #########

INT_MAX = float("inf")
INT_MIN = float("-inf")

# ########## ------ Input Functions ---- #########

input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


# ########## ------ Code ------- ##########

def go(i, j, dp):
    global nums
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    ans = sys.maxsize
    for k in range(i, j):
        temp = go(i, k, dp) + (nums[i - 1] * nums[k]
                               * nums[j]) + go(k + 1, j, dp)
        ans = min(ans, temp)
    dp[i][j] = ans
    return dp[i][j]


t = inp()
while t:
    j = inp() - 1
    nums = inlt()
    dp = [[-1] * (j + 1)for i in range(j + 1)]
    i = 1
    print(go(i, j, dp))

    t -= 1
