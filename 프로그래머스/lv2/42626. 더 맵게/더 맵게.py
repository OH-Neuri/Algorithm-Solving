from heapq import *

def solution(scoville, K):
    cnt=0
    heapify(scoville)
    while scoville[0]<K and len(scoville)>1:
        sco1 = heappop(scoville)
        sco2 = heappop(scoville)
        heappush(scoville, sco1+sco2*2)
        cnt+=1
    return cnt if scoville[0]>=K else -1 
    
        