def bubble (a):
    n=len(a)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if a[j]> a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
arr=list(map(int,input().split()))
print(*(bubble(arr)))


