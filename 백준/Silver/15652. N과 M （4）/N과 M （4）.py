N ,M = map(int,input().split())
# 4 2
# 재귀함수 현재의 나 ,호출 다음의 너
# 현재의 내가 너한테 어떻게 줘야하는가
answer = [0] * M

#현재의 나
def com(depth,idx):
    if depth==M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(idx, N):
        answer[depth] = i+1
        # 다음의 너
        com(depth+1,i)

com(0,0)