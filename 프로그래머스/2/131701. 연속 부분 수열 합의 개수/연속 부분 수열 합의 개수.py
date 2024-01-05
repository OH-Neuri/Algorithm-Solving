def solution(elements):
    l = len(elements)
    tmp_elements = elements[:] + elements[:]
    sub_list = elements[:]
    sub_list.append(sum(elements))
    
    for i in range(2,l):
        s, e = 0, i
        while (l*2)-s >0 and e <= (l*2):
            sub_list.append(sum(tmp_elements[s:e]))
            s+=1
            e+=1
            
    return len(set(sub_list))
