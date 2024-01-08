from heapq import heapify, heappop, heappush
def solution(operations):
    answer = [0,0]
    min_heap = []
    max_heap = []
    
    for i in operations:
        i = i.split(" ")
        w = i[0] # 연산
        v = int(i[1]) # 값
        
        # 삽입
        if w == "I":
            heappush(min_heap,v)
            heappush(max_heap,-v)
            
        # 삭제
        if w == "D" and min_heap: 
            # 최댓값 삭제 
            if v == 1:
                d = heappop(max_heap)
                min_heap.remove(-d)
            # 최솟값 삭제
            if v == -1:
                d = heappop(min_heap)
                max_heap.remove(-d)
        
    if not min_heap:
        return [0,0]
    else:
        return [max(min_heap), min(min_heap)]

