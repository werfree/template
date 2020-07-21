def binarySearch(a, l, r):
    print(l, r)
    if l == r:
        return l
    elif r - l == 1:
        return (l if a[l] < a[r] else r)
    elif l < r:
        mid = (l + r) // 2
        if a[mid] < a[mid - 1] and a[mid] < a[mid + 1]:
            return mid
        if (a[0] < a[mid] < a[-1]):
            return 0
        elif a[mid] > a[0]:
            return binarySearch(a, mid + 1, r)
        elif a[mid] < a[0]:
            return binarySearch(a, l, mid - 1)

        else:
            print("odd", mid)
            return 0

    else:
        print("else")
        return res


def reverseBinarySearch(a, l, r, x):
    if l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return reverseBinarySearch(a, mid + 1, r, x)
        else:
            return reverseBinarySearch(a, l, mid - 1, x)
    return -1


t = int(input())
while t:
    res = -1
    # n = int(input())
    a = list(map(int, input().split()))
    k = (binarySearch(a, 0, len(a) - 1))
    print(k)

    t -= 1
