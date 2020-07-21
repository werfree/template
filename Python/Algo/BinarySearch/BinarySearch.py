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

    n = int(input())
    a = list(map(int, input().split()))
    print(reverseBinarySearch(a, 0, len(a) - 1, n))
    t -= 1
