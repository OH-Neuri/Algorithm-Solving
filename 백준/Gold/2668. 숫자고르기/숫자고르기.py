import sys
input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    adj[i].append(int(input()))

def dfs(num):
    if visited[num] == False:
        visited[num] = True
        for a in adj[num]:

            tmp_up.add(num)
            tmp_bottom.add(a)

            if tmp_up == tmp_bottom:
                ans.extend(list(tmp_bottom))
                return

            dfs(a)
    visited[num] = False

ans = []

for i in range(1, N + 1):
    visited = [False] * (N + 1)  # 위에 값 기준으로
    tmp_up = set()
    tmp_bottom = set()

    dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for a in ans:
    print(a)