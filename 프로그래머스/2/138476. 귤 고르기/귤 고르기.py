from collections import Counter
def solution(k, tangerine):
    answer = 0
    t_cnt = sorted(Counter(tangerine).items(), key = lambda x:x[1],reverse=True)

    sum_cnt = 0
    for size, cnt in t_cnt:
        k-= cnt
        sum_cnt +=1
        if k<=0:
            break
            
    return sum_cnt