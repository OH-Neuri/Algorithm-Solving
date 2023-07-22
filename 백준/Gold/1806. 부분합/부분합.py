import sys
input = sys.stdin.readline

N, S = map(int,input().split())
nums = list(map(int,input().split()))

# 부분합 배열
s = 0
for i in range(N):
    s += nums[i]
    nums[i] = s

min_len = 1e9
left, right = -1, 0
while right<N and left<=right:
    if left ==-1:
        s = nums[right]
    else:
        s = nums[right] - nums[left]
    # 부분합이 S이고 길이가 가장 짧다면
    if s >= S:
        min_len = min(min_len, right-left)
        left+=1
    else:
        right+=1

if min_len == 1e9:
    print(0)
else:
    print(min_len)


