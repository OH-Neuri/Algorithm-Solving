import heapq
def solution(scoville, K):
    # 1. 최소힙 만든다
    # 2. 배열의 최솟값이 K이상 될때까지 while 
    # 3. 배열 스코빌 계산 작업
    # 4. cnt 체크
    heapq.heapify(scoville)
    answer = 0
    while scoville[0]<K and 2<=len(scoville) :
        answer += 1
        scoville_1 = heapq.heappop(scoville)
        scoville_2 = heapq.heappop(scoville)
        heapq.heappush(scoville,(scoville_1+(scoville_2*2)))
        
    if scoville[0]>=K:
        return answer
    else: return -1

print(solution([0,1],2))
        