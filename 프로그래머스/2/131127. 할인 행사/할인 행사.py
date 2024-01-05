def solution(want, number, discount):
    answer = 0
    dic = {}
    for item, num in zip(want, number):
        dic[item] = num
    
    for i in range(len(discount)-9):
        item_cnt = 0
        tmp_dict = dic.copy()
        for j in range(i,i+10):
            if discount[j] not in tmp_dict.keys():
                continue
            elif 0 < tmp_dict[discount[j]]:
                item_cnt+=1
                tmp_dict[discount[j]]-=1
        
        if item_cnt==10:
            answer+=1
            
    return answer

