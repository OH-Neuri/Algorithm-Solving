import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    # 처음부터 되는 경우
    min_food = heapq.heappop(scoville)
    if min_food >= K:
        return answer
    else:
        heapq.heappush(scoville,min_food)
    
    # 음식 섞기
    flag = False
    while 2 <= len(scoville):
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        heapq.heappush(scoville, food1+(food2*2))
        answer +=1
        
        min_food = heapq.heappop(scoville)
        if min_food >= K:
            flag = True
            break
        heapq.heappush(scoville, min_food)
        
    if flag: 
        return answer
    else:
        return -1
        
