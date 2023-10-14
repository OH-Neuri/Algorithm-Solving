from collections import Counter
def solution(weights):
    answer = 0
    # 1:1
    counter = Counter(weights)
    for k,v in counter.items():
        # 같은게 2개 이상있을 때 
        if v>=2:
            answer+= v*(v-1)//2
    weights = set(weights) 
    # print(weights)
    # print(counter)
    
    # 2:3 2:4 3:4 
    for w in weights:
        if w*2/3 in weights:
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]
    return answer