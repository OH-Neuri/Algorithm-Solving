from heapq import heapify, heappop, heappush
def solution(operations):
    max_heap = []
    min_heap = []
    
    for operation in operations:
        operation = operation.split(" ")
        o = operation[0]
        v = int(operation[1])
        
        if o == 'I':    # 삽입
            heappush(max_heap,-v)
            heappush(min_heap,v)
        elif o == "D" and len(min_heap)!=0:   # 삭제
            if v == 1:
                max_value = heappop(max_heap)
                min_heap.remove(-max_value)
            else:
                min_value = heappop(min_heap)
                max_heap.remove(-min_value)

    return  [0,0] if len(min_heap)==0 else [-heappop(max_heap),heappop(min_heap)]

