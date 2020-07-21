def mergeSort(a):

    if len(a) > 1:
        mid = len(a) // 2

        L = a[:mid]
        R = a[mid:]

        mergeSort(L)
        mergeSort(R)

        indexL = indexR = indexArray = 0

        while indexL < len(L) and indexR < len(R):

            if L[indexL] < R[indexR]:
                a[indexArray] = L[indexL]
                indexL += 1
            else:
                a[indexArray] = R[indexR]
                indexR += 1
            indexArray += 1

        while indexL < len(L):
            a[indexArray] = L[indexL]
            indexL += 1
            indexArray += 1

        while indexR < len(R):
            a[indexArray] = R[indexR]
            indexR += 1
            indexArray += 1


a = list(map(int, input("Enter Array = ").split()))
mergeSort(a)
print(a)
