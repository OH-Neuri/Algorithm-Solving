from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 퍼즐을 문자열 123456780으로 정렬
nums =""
for i in range(3):
    nums += "".join(list(input().split()))

# 현재 퍼즐의 모습을 key로, 움직인 횟수를 value로 저장
visited = {nums:0}
q = deque([nums])

def BFS():
    while q:
        # 배열, 0의 자리, 카운트 큐에 넣기
        puzzle = q.popleft()
        z = puzzle.index('0')
        cnt = visited[puzzle]

        if puzzle== "123456780":
            return cnt

        x = z // 3
        y = z % 3
        cnt +=1

        for i in range(4):
            nx = x + dy[i]
            ny = y + dx[i]
            # 이동 가능한 위치일 경우
            if 0<=nx<3 and 0<=ny<3:
                # nx, ny를 문자열의 인덱스로 바꾸자
                nz = nx * 3 + ny
                puzzle_list = list(puzzle) # 원소 스와핑을 위해 문자열을 리스트로 바꾼다
                puzzle_list[z], puzzle_list[nz] = puzzle_list[nz] , puzzle_list[z]
                new_puzzle ="".join(puzzle_list)

                if visited.get(new_puzzle,0)==0:
                    visited[new_puzzle] = cnt
                    q.append(new_puzzle)
    return -1

print(BFS())