def partition(l, r, pivot, a):

    while l <= r:
        print(l,r)

        while a[l] < pivot:
            l += 1

        while a[r] > pivot:
            r -= 1

        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1

    return l

def quickSort(l, r, a):

    if l>=r:
        return

    if l < r:

        pivot = a[(l + r) // 2]

        index = partition(l, r, pivot, a)
        print("in")

        quickSort(l, index-1, a)
        quickSort(index, r, a)


a = list(map(int, input("Enter Array = ").split()))
quickSort(0, len(a) - 1, a)
print(a)
