import sys
input = sys.stdin.readline

N, M = map(int,input().split())

nums = list(map(int,input().split()))
left, right = 0, 1

answer = 0
while right<=N and left <=right:
    s = sum(nums[left:right])
    if s == M:
        answer+=1
        right += 1
    elif s < M:
        right +=1
    else:
        left +=1

print(answer)
