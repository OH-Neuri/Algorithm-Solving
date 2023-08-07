def solution(clothes):
    clothes_dict = {}
    for i in range(len(clothes)):
        if clothes[i][1] in clothes_dict.keys():
            clothes_dict[clothes[i][1]] +=1
        else: clothes_dict[clothes[i][1]] =1
    
    answer = 1
    for x in clothes_dict.values():
        answer *=(x+1)
    return answer-1