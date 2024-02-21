import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
edges = []
for _ in range(M):
    A, B, C = map(int,input().split())
    edges.append((A, B, C))

# cost가 낮은 것 부터 정렬
edges.sort(key=lambda x:x[2])

parent = [i for i in range(N+1)]
def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)
    if a < b:  # 작은 쪽이 부모가 된다.
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a,b):
    # 부모가 같으면 True, 다르면 False
    return get_parent(a) == get_parent(b)

answer = 0
for a, b, cost in edges:
    # cost가 작은 간선부터 하나씩 추가
    # 이때 두 노드의 부모가 일치하는 경우 간선을 추가하면 사이클이 발생!
    # 두 노드의 부모가 일치하지 않는 경우에만 간선 추가
    if not same_parent(a,b):
        union_parent(a,b)
        answer += cost

print(answer)