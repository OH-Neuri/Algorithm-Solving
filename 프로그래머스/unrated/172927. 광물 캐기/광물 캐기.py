def solution(picks, minerals):
    answer = 0
    
    # 쓸 수 있는 곡괭이 수
    picks_cnt = 0
    for x in picks:
        picks_cnt += x
    
    # 캘 수 있는 광물 수가 더 많을 경우 
    if picks_cnt *5 < len(minerals):
        # 못 캐는 광물은 버린다
        minerals = minerals[:picks_cnt*5]
    # minerals 에서 광물 개수 정렬
    minerals_sorted = [[0,0,0] for _ in range(len(minerals)//5 + 1)]
    for i in range(len(minerals)):
        if minerals[i]=="diamond":
            minerals_sorted[i//5][0] +=1
        elif minerals[i]== "iron":
            minerals_sorted[i//5][1] +=1
        elif minerals[i]=="stone":
            minerals_sorted[i//5][2] +=1
    
    minerals_sorted = sorted(minerals_sorted, key = lambda x:(-x[0], -x[1], -x[2]))
    for x in minerals_sorted:
        d,i,s = x
        for j in range(len(picks)):
            if j == 0 and picks[j]>0:
                picks[j]-=1
                answer += d + i + s
                break
            elif j == 1 and picks[j]>0:
                picks[j]-=1
                answer += (5*d) + i + s
                break
            elif j == 2 and picks[j]>0:
                picks[j]-=1
                answer += (25*d) + (5*i) + s
                break
                
    return answer