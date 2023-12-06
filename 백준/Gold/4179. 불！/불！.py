from collections import deque
import sys
input = sys.stdin.readline

# 시계방향
dx = [0,1,0,-1]
dy = [1,0,-1,0]

R, C = map(int,input().split())
arr = [] # 미로
J_x, J_y = 0, 0  # 지훈이 위치
q = deque() # 불난곳
j_q = deque()  # 지훈이가 갈 수 있는 경로
fire_visited = [[False]*C for _ in range(R)] # 불난곳 방문처리
j_visited = [[False]*C for _ in range(R)] # 지훈녀석 방문처리
for i in range(R):
    data = list(input().rstrip())
    arr.append(data)
    for idx, j in enumerate(data):
        if j == 'J':
            j_visited[i][idx] = True
            j_q.append((i,idx))
        if j == "F":
            fire_visited[i][idx] = True
            q.append((i,idx))


time = 1
def escape():
    global time

    while True:
        
        # 불이 퍼진다
        fire_tmp = []
        while q:
            x, y = q.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0<=nx<R and 0<=ny<C and not fire_visited[nx][ny] and arr[nx][ny]!='#':
                    fire_visited[nx][ny] = True
                    fire_tmp.append((nx,ny))
        q.extend(fire_tmp)
        
        # 지훈이가 이동한다
        j_tmp = []
        while j_q:
            j_x, j_y = j_q.popleft()

            for k in range(4):
                nx = j_x + dx[k]
                ny = j_y + dy[k]

                # 배열 밖이면 탈출
                if 0>nx or nx>=R or 0>ny or ny>=C:
                    return True
                # 아직 배열 안에 있을 경우
                if arr[nx][ny]!='#' and not fire_visited[nx][ny] and not j_visited[nx][ny]:
                    j_visited[nx][ny] = True
                    j_tmp.append((nx,ny))
        j_q.extend(j_tmp)
        
        # 지훈이가 갈 수 있는 경로가 없을 경우 실패
        if len(j_tmp)==0:
            return False
        time+=1

if escape():
    print(time)
else:
    print('IMPOSSIBLE')
