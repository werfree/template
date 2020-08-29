from functools import cmp_to_key


def comparator(a, b):
    print(a, b)
    if b[0] < a[0]:
        return 1
    if b[0] == a[0]:
        if b[1]-b[0] < a[1]-a[0]:
            return 1
        return -1
    return -1


a = [[1, 4], [2, 5], [3, 4]]

a.sort(key=cmp_to_key(comparator))

print(a)
