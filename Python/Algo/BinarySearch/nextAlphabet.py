
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
    return(list(map(str, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


# ########## ------ Code ------- ##########
def binarySearch(a, l, r, x):
    if l <= r:
        global res
        mid = (l + r) // 2

        if a[mid] == x:
            res = mid
            return mid
        elif a[mid] < x:
            return binarySearch(a, mid + 1, r, x)
        else:
            if res != INT_MIN:
                res = res if a[res] < a[mid] else mid
            else:
                res = mid
            return binarySearch(a, l, mid - 1, x)
    else:
        return -1


t = inp()

while t:
    res = INT_MIN
    n = input()
    a = inlt()
    if n < a[0]:
        print("less")
        print(a[0])
    elif n > a[-1]:
        print("more")
        print(-1)
    else:
        k = (binarySearch(a, 0, len(a) - 1, n))
        print(a[res])

    t -= 1
