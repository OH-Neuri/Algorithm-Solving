from collections import Counter
def solution(k, tangerine):
    count = Counter(tangerine)
    sort = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    answer = 0
    # k = 6, b = 3
    for a, b in sort:
        if b<=k:
            k-=b
            answer+=1
        elif k==0:
            break
        else:
            answer+=1
            break
    return answer