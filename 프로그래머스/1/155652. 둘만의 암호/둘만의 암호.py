def solution(s, skip, index):
    answer =''
    for change_s in s :
        step = 0
        while(step!=index):
            change_s = chr(ord(change_s)+1)
            if change_s=="{" : change_s = 'a'
            
            if change_s in skip:
                continue
            else:
                step +=1
        answer += change_s
    return answer