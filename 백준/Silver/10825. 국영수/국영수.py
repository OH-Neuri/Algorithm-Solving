import sys
input = sys.stdin.readline

N = int(input())
score_list = []

for _ in range(N):
    [name, kor, eng, math] = map(str, input().split())
    score_list.append([name, int(kor), int(eng), int(math)])

score_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]) )

for i in range(N):
    print(score_list[i][0])