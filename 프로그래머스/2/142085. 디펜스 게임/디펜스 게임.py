from heapq import heappop, heappush
from collections import deque, Counter
def solution(n, k, enemy):
    answer = 0
    
    sum_enemy=0
    heap = []
    for x in enemy:
        sum_enemy +=x
        heappush(heap,-x)
        if sum_enemy > n:
            if k==0: break
            else:
                sum_enemy+=heappop(heap)
                k-=1
        answer +=1
    return answer