from collections import deque

gears = []
for _ in range(4):
    gears.append(deque((map(int, list(input())))))

K = int(input())
for _ in range(K):
    idx, dir = map(int, input().split())

    idx -= 1
    rotation = [0] * 4
    rotation[idx] = dir

    for i in range(idx+1, 4):
        if rotation[i-1] and gears[i-1][2] != gears[i][6]:
            rotation[i] = -rotation[i-1]

    for i in range(idx-1, -1, -1):
        if rotation[i+1] and gears[i+1][6] != gears[i][2]:
            rotation[i] = -rotation[i+1]

    for i in range(4):
        gears[i].rotate(rotation[i])

ans = 0
for i in range(4):
    ans += gears[i][0] * pow(2, i)
print(ans)
