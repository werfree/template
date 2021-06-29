def heapify(arr, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    # Check left
    if left < n and arr[largest] < arr[left]:
        largest = left

    # Check right
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        # swap
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def heapSort(arr, n):

    # Create heap

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    print("After heapify", arr)

    # extract 1 by 1
    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    print("Sort", arr)
    return


arr = list(map(int, input().split()))
n = len(arr)

heapSort(arr, n)


# [2, 4, 3, 1, 6, 5, 5]
#  0  1  2  3  4  5  6

#             6
#         5       5
#     1      4   2  3
