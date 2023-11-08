N, M = map(int,input().split())
nums = sorted(list(map(int,input().split())))
answer = [0] * M

def per(depth):
    if depth == M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(N):
        answer[depth] = nums[i]
        per(depth+1)

per(0)