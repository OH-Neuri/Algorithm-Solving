from heapq import heappush,heappop,heapify
import sys
input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    n = int(input())
    heap.append(n)

heapify(heap)
result = 0
for _ in range(N-1):
    a = heappop(heap)
    b = heappop(heap)
    result += a+b
    heappush(heap,a+b)

print(result)