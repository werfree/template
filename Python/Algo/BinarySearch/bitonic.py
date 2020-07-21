
# ########## ------ Code ------- ##########

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

def binarySearch(a, l, r):
    print(l, r)
    if l <= r:
        mid = (l + r) // 2
        if (a[mid] > a[mid + 1]) and (a[mid] > a[mid - 1]):
            return a[mid]
        elif a[mid] > a[mid - 1]:
            return binarySearch(a, mid + 1, r)
        else:
            return binarySearch(a, l, mid - 1)
    else:
        return -1


t = int(input())

while t:

    n = inlt()
    if n[0] > n[1]:
        print(n[0])
    elif n[-1] > n[-2]:
        print(n[-1])
    else:
        print(binarySearch(n, 1, len(n) - 2))

    t -= 1
