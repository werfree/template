
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

def binarySearch(a, l, r, x):

    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return mid
        elif a[mid + 1] == x:
            return mid + 1
        elif a[mid - 1] == x:
            return mid - 1
        elif a[mid] < x:
            l = mid + 2
        else:
            r = mid - 2
    return -1


t = inp()
while t:

    n = inp()
    a = inlt()
    print(binarySearch(a, 0, len(a), n))

    t -= 1
