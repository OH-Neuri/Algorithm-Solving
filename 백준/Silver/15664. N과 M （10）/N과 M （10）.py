N, M = map(int,input().split())
nums = list(map(int,input().split()))
count = [0] * 10050
answer = [0] * M

for num in nums:
    count[num] +=1

def com(depth, idx):
    if depth == M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(idx,10001):
        if count[i+1] > 0:
            answer[depth] = i+1
            count[i+1]-=1
            com(depth+1,i)
            count[i+1]+=1
com(0,0)