import sys

n, l = map(int, sys.stdin.readline().rsplit())
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
answer = 0

def solve(y, x, val, cnt):
    if x == n: return True
    if arr[y][x] == val: cnt += 1
    elif abs(arr[y][x]-val) > 1: return False
    elif val < arr[y][x]:
        if cnt < l: return False
        val = arr[y][x]
        cnt = 1
    
    elif val > arr[y][x]:
        k = 0
        cnt = 0
        for k in range(x, n):
            if arr[y][k] == arr[y][x]: cnt += 1
            else: break

            if cnt == l: break

        val = arr[y][x]
        if cnt < l: return False
        x = k
        cnt = 0
    
    return solve(y, x+1, val, cnt)

for i in range(n):
    if solve(i, 1, arr[i][0], 1): answer += 1
    
arr = [[arr[j][i] for j in range(n)] for i in range(n)]
for i in range(n):
    if solve(i, 1, arr[i][0], 1): answer += 1

print(answer)