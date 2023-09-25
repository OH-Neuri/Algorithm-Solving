from collections import deque
import math

def solution(stones, k):
    max_arr = []

    q = deque()
    q.append((-stones[0], 0))
    max_arr.append(stones[0])

    for i in range(1, len(stones)):
        tmp = stones[i]

        while q and -q[-1][0] < tmp:
            q.pop()

        q.append((-stones[i], i))

        while i - q[0][1] >= k:
            q.popleft()

        max_arr.append(-q[0][0])

    return min(max_arr[k-1:])