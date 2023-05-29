def solution(num_list):
    a = len(list(filter(lambda v: v% 2 ==0, [i for i in num_list])))
    b = len(list(filter(lambda v: v% 2 == 1, [j for j in num_list])))
    answer = [a,b]
    return answer 