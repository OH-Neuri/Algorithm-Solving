import sys
input = sys.stdin.readline

direction = ("U", "R", "D", "L")
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
P, Q = (1, 0, 3, 2), (3, 2, 1, 0)

N, M = map(int, input().split())
A = [["C"] * (M+2)]     # 블랙홀로 둘러싸기
for _ in range(N):
    A.append(["C"] + list(input().strip()) + ["C"])
A.append(["C"] * (M+2))
sr, sc = map(int, input().split())

def solve():
    max_time, max_dir = 0, 0
    for sd in range(4):
        r, c, d, time = sr, sc, sd, 1   # 시작 위치, 시작 방향, 이동 시간
        while True:
       		# 블랙홀 만났거나 항성계 벗어나면
            if A[r+dr[d]][c+dc[d]] == "C":
                break
            
            r += dr[d]
            c += dc[d]

            # 방향 전환
            if A[r][c] == "/":
                d = P[d]
            elif A[r][c] == "\\":
                d = Q[d]
            time += 1

            # 처음 출발한 지점을 동일한 방향으로 접근한 경우 무한 루프
            if (r, c, d) == (sr, sc, sd):
                print(direction[sd])
                print("Voyager")
                return

        # 값이 클 때만 이동 시간, 현재 방향 갱신
        if max_time < time:
            max_time = time
            max_dir = sd

    print(direction[max_dir])
    print(max_time)

solve()