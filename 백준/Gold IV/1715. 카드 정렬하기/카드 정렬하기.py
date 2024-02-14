from heapq import heappush,heappop,heapify
N = int(input())
heap = []
heapify(heap)
for _ in range(N):
    n = int(input())
    heappush(heap,n)

result = 0
for _ in range(N-1):
    a = heappop(heap)
    b = heappop(heap)
    result += a+b
    heappush(heap,a+b)

print(result)