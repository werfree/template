
def mergeSort(a):
    if len(a) > 1:
        mid = len(a) // 2

        L = a[:mid]
        R = a[mid:]
        mergeSort(L)
        mergeSort(R)

        indexL = indexR = k = 0

        while indexL < len(L) and indexR < len(R):
            if L[indexL] < R[indexR]:
                a[k] = L[indexL]
                indexL += 1
            else:
                a[k] = R[indexR]
                indexR += 1
            k += 1
        while indexL < len(L):
            a[k] = L[indexL]
            k += 1
            indexL += 1

        while indexR < len(R):
            a[k] = R[indexR]
            k += 1
            indexR += 1


a = [1, 2, 3, 3, 2, 1]
mergeSort(a)
print(a)
