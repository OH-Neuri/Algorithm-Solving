def solution(s):
    change_cnt = 0
    zero_cnt = 0     
    while s!='1':
        zero_cnt += s.count("0")    
        s = bin(len(s.replace("0","")))[2:]
        change_cnt +=1
    return [change_cnt,zero_cnt]