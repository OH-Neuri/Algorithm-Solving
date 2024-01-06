from itertools import permutations
def solution(k, dungeons):
    l = len(dungeons)
    per = list(permutations([i for i in range(l)],l))
    
    answer = 0
    for sequence in per:
        tmp_k = k
        cnt = 0
        for i in sequence:
            # 던전 돌기
            if tmp_k >= dungeons[i][0]:
                tmp_k-= dungeons[i][1]
                cnt+=1
                
                # 던전을 다 돌았을 경우
                if cnt == l:
                    answer = cnt
            else:
                # 필요도가 부족한 경우
                answer = max(cnt,answer)
                break
    return answer