def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        # 1이면 0, 0이면 1
        k = int(i!=1)
        max_num = 1
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                if (i//j)<=10000000:
                    k=i//j
                    break
                else:
                   max_num  = j  
        if k == 1 :
            answer.append(max_num)
        else:
            answer.append(k)
        
    return answer