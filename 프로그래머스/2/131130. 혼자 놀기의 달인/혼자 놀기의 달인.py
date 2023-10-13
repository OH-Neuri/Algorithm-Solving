from collections import Counter
def solution(cards):
    l = len(cards)
    visited = [0] * l
    answer = 0
    
    # i : 박스번호
    def Box(i):
        check = cards[i]-1
        while not visited[check]:
            visited[check] = i+1
            check = cards[check]-1
            
        
    for i in range(l):
        if visited[i] == 0:
            Box(i)
    
    counter = sorted(Counter(visited).items(), key=lambda x:x[1], reverse=True)
    
    return (counter[0][1] * counter[1][1]) if len(counter)>1 else 0