import sys
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

# ✨ DFS
def DFS(x,y,L,total):
    global res
    if res >= total + max_pos*(4-L):
        return #  예외처리
    if L == 4:
        res = max(res,total)
        return #  4칸을 돌면 == 테트로미노를 만들면
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny] == 0:
                if L == 2: # 2번째 테트로미노에서
                    visit[nx][ny] = 1
                    DFS(x,y,L+1,total+board[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                DFS(nx,ny,L+1,total+board[nx][ny])
                visit[nx][ny] = 0
            
max_pos = max(map(max,board)) 
res = 0
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        DFS(i,j,1,board[i][j])
        visit[i][j] = 0
print(res)