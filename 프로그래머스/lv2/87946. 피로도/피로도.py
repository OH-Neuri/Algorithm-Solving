import itertools
def solution(k, dungeons):
    per = list(itertools.permutations(dungeons,len(dungeons)))
    answer = 0
    for i in range(len(per)):
        cnt = 0
        k_copy = k
        for a, b in per[i]:
            if a <= k_copy:
                k_copy-=b
                cnt+=1
        answer = max(answer,cnt)
    
    return answer