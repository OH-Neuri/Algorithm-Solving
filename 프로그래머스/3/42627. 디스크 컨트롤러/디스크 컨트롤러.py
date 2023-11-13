import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap,[j[1],j[0]])
        if len(heap) > 0:
            curr = heapq.heappop(heap)
            start = now
            now += curr[0]
            answer += (now - curr[1])
            i +=1
        else:
            now +=1
    
    return int(answer / len(jobs)) 