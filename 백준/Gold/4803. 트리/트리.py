import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(node, prev):
    global flag
    visited[node] = True
    
    for next in graph[node]:
        if next == prev:
            continue
        if not visited[next]:
            DFS(next,node)
        else:
            flag = True

n, m = map(int,input().split())
tc = 1
while n!=0 or m!= 0:
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        s, e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    tree_cnt = 0

    for i in range(1,n+1):
        flag = False
        if not visited[i]:
            DFS(i,0)
            if not flag:
                tree_cnt += 1

    if tree_cnt == 0:
        print(f'Case {tc}: No trees.')
    elif tree_cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {tree_cnt} trees.')

    tc +=1
    n, m = map(int,input().split())
