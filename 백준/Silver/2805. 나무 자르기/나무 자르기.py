import sys
input = sys.stdin.readline

N, M = map(int,input().split(" "))
tree = list(map(int,input().split(" ")))
start, end = 1, max(tree)

while start<=end:
    mid = (start+end)//2
    m = 0
    for x in tree:
        if x>mid:
            m += x-mid
    if m>=M:
        start = mid + 1
    else:
        end = mid -1
print(end)

