def solution(s):
    x = ''
    x_cnt = 0
    y_cnt = 0
    answer = 0
    
    for word in s:
        if x=='':
            x = word
        if x!='' and word == x:
            x_cnt += 1
        elif x!='' and word!=x:
            y_cnt +=1
        
        if x_cnt==y_cnt:
            answer +=1
            x_cnt, y_cnt = 0, 0
            x = ''
            
    if x!='':
        answer+=1
    return answer