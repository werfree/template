
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

def go(i, j, y):
    if i > j:
        return 0
    if d.get((i, j, y)):
        return d.get((i, j, y))
    d[i, j, y] = max(a[i] * y + go(i + 1, j, y + 1),
                     a[j] * y + go(i, j - 1, y + 1))
    return d[i, j, y]


t = inp()
while t:

    n = inp()
    a = inlt()
    d = dict()
    print(go(0, n - 1, 1))

    t -= 1
