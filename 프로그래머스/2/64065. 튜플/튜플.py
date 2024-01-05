import re
def solution(s):
    answer = []
    s = s[1:-1]
    
    flag = 0
    num_list = []
    for i in range(len(s)):
        if s[i] == '}':
            num = re.findall('\d+',s[flag:i])
            num_list.append(list(map(int,num)))
            flag = i
    
    num_list.sort(key = lambda x:len(x))
    
    for i in range(len(num_list)):
        for j in range(len(num_list[i])):
            if not num_list[i][j] in answer:
                answer.append(num_list[i][j])
    return answer
