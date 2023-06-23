import sys

input = sys.stdin.readline

nums = list(str(input().strip()))
dp = [0 for _ in range(len(nums) + 1)]
dp[0], dp[1] = 1, 1
if nums[0] == '0':
    print(0)
else:
    for i in range(2, len(nums) + 1):
        if int(nums[i - 1]) > 0:
            dp[i] += dp[i - 1]
        to_int = int(nums[i - 2] + nums[i - 1])
        if 10 <= to_int <= 26:
            dp[i] += dp[i - 2]
    print(dp[len(nums)] % 1000000)