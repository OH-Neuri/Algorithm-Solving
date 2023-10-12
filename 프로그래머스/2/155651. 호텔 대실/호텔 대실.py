from heapq import heappop, heappush
def solution(book_time):
    idx = 0
    answer = 1
    for start_time, end_time in book_time:
        start = int(start_time[:2])*60 + int(start_time[3:])
        end = int(end_time[:2])*60 + int(end_time[3:])
        book_time[idx][0] = start
        book_time[idx][1] = end
        idx+=1
    book_time.sort()
    
    heap = []
    for s, e in book_time:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e+10)
    
    return answer