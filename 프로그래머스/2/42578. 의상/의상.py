def solution(clothes):

    clothes_dict = {}
    for item, item_type in clothes:
        if item_type not in clothes_dict.keys():
            clothes_dict[item_type] =1
        else:
            clothes_dict[item_type] +=1
    
    answer = 1
    for cnt in clothes_dict.values():
        answer*=(cnt+1)
        
    return answer -1