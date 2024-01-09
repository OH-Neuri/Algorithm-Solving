from heapq import heappop, heappush, heapify
def solution(n, works):
    if sum(works) <= n:
        return 0
    
    # max heap
    works = [-x for x in works]
    heapify(works)
    
    for _ in range(n):
        i = heappop(works)
        i +=1
        heappush(works,i)
    
    return sum([x**2 for x in works])