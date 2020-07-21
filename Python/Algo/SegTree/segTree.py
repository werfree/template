import sys

input = sys.stdin.readline
MAX = sys.maxsize


def build(index, left, right):
    if left == right:
        segTree[index] = a[left]
        return

    mid = (left+right)//2
    build((index*2)+2, mid+1, right)
    build((index*2)+1, left, mid)
    segTree[index] = min(segTree[(2*index)+1], segTree[(2*index)+2])


def quary(index, range_l, range_r, left, right):

    # Completely Inside
    if range_l <= left and range_r >= right:
        return segTree[index]

    # Completely Outside
    if range_l > right or range_r < left:
        return MAX

    # Overlape
    mid = (left+right)//2
    leftTree = quary(index*2+1, range_l, range_r, left, mid)
    rightTree = quary(index*2+2, range_l, range_r, mid+1, right)
    return min(leftTree, rightTree)


def update(index, left, right, i, value):
    if left == right:
        a[i] = value
        segTree[index] = value
        return

    mid = (left+right)//2
    if i <= mid:
        update(index*2+1, left, mid, i, value)
    else:
        update(index*2+2, mid+1, right, i, value)

    leftT = seg[index*2+1]
    rightT = seg[index*2+2]

    segTree[index] = min(leftT, rightT)

    seg[index] = [leftEve+rightEve, leftOdd+rightOdd]


n = int(input())
a = list(map(int, input().split()))

l = 0
r = n

segTree = [MAX]*(4*r)

build(0, l, r-1)

n = int(input())
while n:
    # quary 0 index
    q = list(map(int, input().split()))
    print(quary(0, q[0], q[1], 0, r-1))
    n -= 1
