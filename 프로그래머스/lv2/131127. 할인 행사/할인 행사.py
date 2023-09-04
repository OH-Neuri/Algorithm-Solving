import copy
def solution(want, number, discount):
    want_list ={}
    answer = 0
    # wan_list 딕셔너리 저장
    for x in range(len(want)):
        want_list[want[x]] = number[x]
    #다 0될때까지10개씩 잘라서 확인
    for x in range(len(discount)-9): 
        cnt=0
        want_copy= copy.deepcopy(want_list)
        for b in range(x,x+10):
            if discount[b] in want_copy.keys():
                if want_copy[discount[b]] > 0:
                    want_copy[discount[b]] -= 1
                    cnt+=1
        if cnt ==10:
            answer +=1
    return answer