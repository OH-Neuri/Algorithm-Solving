from itertools import permutations
def solution(k, dungeons):
    result = 0
    
    for index_arr in permutations([i for i in range(len(dungeons))]):
        tmp_k = k 
        go = 0
        for idx in index_arr: 
            if tmp_k >= dungeons[idx][0]:
                tmp_k -= dungeons[idx][1]
                go += 1
        result = max(go, result)
        
    return result