from collections import deque
def solution(maps):
    answer = 0
    # BFS 최솟값, 못가면 -1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    N = len(maps)
    M = len(maps[0])
    visited= [[False for _ in range(M)] for _ in range(N)]
    
    def BFS(i,j,n,m):
        q = deque()
        q.append((i,j,1))
        visited[i][j] = True

        while q:
            x, y, cnt = q.popleft()
            if x == n-1 and y == m-1:
                return cnt

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx,ny,cnt+1))
        return -1
    
    answer = BFS(0,0,N,M)
    return answer