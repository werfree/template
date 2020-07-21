
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
    a = inlt()

    global_length = INT_MIN
    global_index = 0
    local_length = 0
    for i in range(0, len(a)):
        if a[i]:
            local_length += 1
        else:
            local_length -= 1

        if local_length == 0:
            global_length = i + 1
        0

    t -= 1
