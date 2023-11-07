N, M = map(int,input().split())
nums = sorted(list(map(int,input().split())))
visit = [False] * N
answer = [0] * M
def per(depth):
    if depth == M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(N):
        if not visit[i]:
            answer[depth] = nums[i]
            visit[i] = True
            per(depth+1)
            visit[i] = False
per(0)

