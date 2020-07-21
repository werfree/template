
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
    if l <= r:
        global res
        mid = (l + r) // 2

        if a[mid] == x:
            res = mid
            return mid
        elif a[mid] < x:

            if a[mid] < x:
                if res != INT_MIN:
                    res = res if a[res] > a[mid] else mid
                else:
                    res = mid
            return binarySearch(a, mid + 1, r, x)
        else:
            return binarySearch(a, l, mid - 1, x)
    else:
        return -1


t = inp()

while t:
    res = INT_MIN
    n = inlt()
    a = inlt()
    if n[1] < a[0]:
        print(-1)
    elif n[1] > a[-1]:
        print(n[0] - 1)
    else:
        k = (binarySearch(a, 0, n[0] - 1, n[1]))
        print(res)

    t -= 1
