import heapq
def solution(operations):
    min_heapq = []
    max_heapq = []

    answer = []
    for a in operations:
        a = a.split(" ")
        if a[0] == 'I':
            num = int(a[1])
            heapq.heappush(min_heapq,num)
            heapq.heappush(max_heapq,-num)
        else:
            if len(min_heapq) == 0:
                pass
            elif a[1] == '-1':
                m = heapq.heappop(min_heapq)
                max_heapq.remove(-m)
            elif a[1] == '1':
                M = heapq.heappop(max_heapq)
                min_heapq.remove(-M)
    if min_heapq:
        return [-heapq.heappop(max_heapq),heapq.heappop(min_heapq)]
    else:
        return [0,0]
