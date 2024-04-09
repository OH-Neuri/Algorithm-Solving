from heapq import heappop, heappush
def solution(book_time):
    heap = []
    book_time = [[time_to_minutes(start), time_to_minutes(end)] for start, end in book_time]
    book_time = sorted(book_time, key=lambda x: x[0])
    answer = 0
    
    for start, end in book_time:
        if not heap:
            heappush(heap, end+10)
            answer +=1
            continue
            
        early_time = heappop(heap)
        if early_time > start:
            answer +=1
            heappush(heap,early_time)
        heappush(heap,end+10)
        
    return answer

def time_to_minutes(time_str):
    hour, minute = map(int, time_str.split(':'))
    return hour * 60 + minute