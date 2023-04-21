import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# 트리 정점의 개수
n = int(input())
# 트리
tree = [[] for _ in range(n+1)]
# 트리 방문 순서
treeVisited = [[] for _ in range(n+1)]
# 방문 체크
visited = [0]*(n+1)
# 방문 카운트 변수
cnt = 1

for i in range(n):
    node = list(map(int,input().split()))
    tree[node[0]] = node[1:-1]

root = int(input())
visited[root]=1


def dfs(v):
    global cnt
    treeVisited[v].append(cnt)
    edges = sorted(tree[v])
    for x in edges:
        if visited[x] == 0:
            visited[x] = 1
            cnt+=1
            dfs(x)
    cnt+=1
    treeVisited[v].append(cnt)


dfs(root)

for i in range(1,len(treeVisited)):
    print(i,treeVisited[i][0],treeVisited[i][1])
