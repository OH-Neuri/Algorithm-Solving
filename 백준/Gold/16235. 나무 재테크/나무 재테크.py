import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

n, m, k = map(int, input().split())
plus_a = [list(map(int, input().split())) for _ in range(n)]
a = [[5]*n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

for year in range(k):

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                temp_tree, dead_tree = [], 0
                for age in tree[i][j]:
                    if age <= a[i][j]:
                        a[i][j] -= age
                        age += 1
                        temp_tree.append(age)
                    else:
                        dead_tree += age // 2
                a[i][j] += dead_tree
                tree[i][j] = []
                tree[i][j].extend(temp_tree)

    if not tree:
        print(0)
        sys.exit()

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for dir in range(8):
                            ni = i + dx[dir]
                            nj = j + dy[dir]
                            if 0 <= ni < n and 0 <= nj < n:
                                tree[ni][nj].append(1)

    for i in range(n):
        for j in range(n):
            a[i][j] += plus_a[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)