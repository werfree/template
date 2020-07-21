def binarySearch(a, l, r, x):
    if l <= r:
        mid = (l + r) // 2

        if a[mid] == x:
            return mid
        elif a[mid] < x:
            return binarySearch(a, mid + 1, r, x)
        else:
            return binarySearch(a, l, mid - 1, x)
    else:
        return -1


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


t = inp()
while t:

    n = inp()
    a = inlt()
    print(binarySearch(a, 0, len(a) - 1, n))
    t -= 1

    pass
