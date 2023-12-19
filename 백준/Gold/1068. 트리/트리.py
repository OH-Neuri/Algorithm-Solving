import sys
input = sys.stdin.readline

def dfs(v):
    for i in child[v]:
        dfs(i)
    child[v] = "del"

n = int(input())
arr = list(map(int,input().split()))
d = int(input())
child = [[] for _ in range(n)]
ans = 0

# 부모 -> 자식 방향의 간선 배열을 생성
for i in range(n):
    if arr[i] == -1:
        continue
    child[arr[i]].append(i)

# 간선 배열을 바탕으로 지울 노드의 자식을 모조리 삭제
dfs(d)

# 부모 노드에서 지울 노드를 없애줌.
try:
    child[arr[d]].remove(d)
except:
    pass

for i in child:
    if not i:
        ans+=1
print(ans)