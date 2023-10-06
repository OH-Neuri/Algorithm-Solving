def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        # 스택이 비어있는 경우 일단 넣는다.
        if not answer:
            answer.append(num)
            continue
        # 지울 기회가 남아있다면,
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)