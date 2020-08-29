'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   _____ ___                     __                 ________  __           __
  / ___//   | __  ______ _____  / /_____ _____     / ____/ / / /___  _____/ /_
  \__ \/ /| |/ / / / __ `/ __ \/ __/ __ `/ __ \   / / __/ /_/ / __ \/ ___/ __ \
 ___/ / ___ / /_/ / /_/ / / / / /_/ /_/ / / / /  / /_/ / __  / /_/ (__  ) / / /
/____/_/  |_\__, /\__,_/_/ /_/\__/\__,_/_/ /_/   \____/_/ /_/\____/____/_/ /_/
           /____/

             **************************************************
                   _  _  ____  ____  ____  ____  ____  ____
                  / )( \(  __)(  _ \(  __)(  _ \(  __)(  __)
                  \ /\ / ) _)  )   / ) _)  )   / ) _)  ) _)
                  (_/\_)(____)(__\_)(__)  (__\_)(____)(____)

            ***************************************************


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


# ########## ------ Import ------- ##########

import sys
import math
from collections import Counter, defaultdict
from collections import deque as deq
from functools import lru_cache
from copy import deepcopy
from pprint import pprint as print

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

def main():
    t = inp()
    while t:
        n = insr()

        start = end = 0
        length = len(n)
        d = default
        while end < length:


main()
