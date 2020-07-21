def selection(a):
    n = len(a)
    for i in range(0, n):
        small = i
        for j in range(i+1, n):
            if a[j] < a[small]:
                small = j
        a[i], a[small] = a[small], a[i]
    return a
arr= list(map(int, input().split()))
print(*(selection(arr)))

