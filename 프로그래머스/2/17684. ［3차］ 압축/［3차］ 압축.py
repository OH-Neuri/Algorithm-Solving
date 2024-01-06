def solution(msg):
    answer = []
    T = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {}
    for i in range(len(T)):
        dic[T[i]] = i+1
    
    l = len(msg)
    number = 26
    
    pass_cnt = 0
    i = 0
    while i != len(msg):
        pass_cnt = 0
        for j in range(i, l):
            if msg[i:j+1] not in dic.keys():
                number +=1
                dic[msg[i:j+1]] = number
                answer.append(dic[msg[i:j]])
                break
            else:
                if j+1 == l:
                    answer.append(dic[msg[i:j+1]])
                pass_cnt +=1
        i += 1 + pass_cnt -1
                
    return answer

