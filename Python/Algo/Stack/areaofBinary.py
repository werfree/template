
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


def sRight(l, a):
    d = deq()
    k = [-1] * l
    for i in range(l - 1, -1, -1):
        found = False
        if d:
            while d:
                if(a[d[-1]] < a[i]):
                    k[i] = d[-1]
                    d.append(i)
                    found = True
                    break
                else:
                    d.pop()
            if not found:
                k[i] = i
                d.append(i)

        else:
            k[i] = i
            d.append(i)
    return k


def sLeft(l, a):
    d = deq()
    k = [-1] * l
    for i in range(0, l):
        found = False
        if d:
            while d:
                if(a[d[-1]] < a[i]):
                    k[i] = d[-1]
                    d.append(i)
                    found = True
                    break
                else:
                    d.pop()
            if not found:
                k[i] = i
                d.append(i)

        else:
            k[i] = i
            d.append(i)

    return k


def mah(a, n):
    smallLeft = sLeft(n, a)
    smallRight = sRight(n, a)
    ans = INT_MIN
    for i in range(0, n):
        if smallLeft[i] == i:
            tempLeft = -1
        else:
            tempLeft = smallLeft[i]
        if smallRight[i] == i:
            tempRight = n - 1
        else:
            tempRight = smallRight[i] - 1
        print(a[i], smallLeft[i], smallRight[i])
        print(a[i], tempLeft, tempRight)
        print(a[i], (abs(tempRight - tempLeft)) * a[i])
        print()
        ans = max(ans, (abs(tempRight - tempLeft)) * a[i])
    return(ans)


while t:

    n = inlt()
    a = inlt()
    s = 0
    e = n[0]
    b = []
    count = -0
    ans = INT_MIN
    for i in range(0, n[0]):
        c = []
        for j in range(n[1]):
            c.append(a[count])
            count += 1
        b.append(c)
    for i in b:
        print(i)
    for i in range(1, n[0]):
        for j in range(0, n[1]):
            if b[i][j]:
                b[i][j] = b[i][j] + b[i - 1][j]
            else:
                b[i][j] = 0
    for i in b:
        ans = max(ans, mah(i, n[1]))
    print(ans)

    t -= 1
