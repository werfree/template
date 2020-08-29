# ########## ------ Import ------- ##########

from sys import maxsize, stdin
from math import log, pow, sqrt, floor, ceil
from collections import Counter, defaultdict
from collections import deque as deq
from functools import lru_cache
from itertools import permutations as perm
from itertools import combinations as comb
from itertools import combinations_with_replacement as combr

# ########## ------ Define -------- #########

INF = 2147483647
PI = 3.141592653589793
MOD = 1000000007

# ########## ------ Input Functions ---- #########

input = stdin.readline


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

        n = inp()
        a = inlt()

        t -= 1


main()
