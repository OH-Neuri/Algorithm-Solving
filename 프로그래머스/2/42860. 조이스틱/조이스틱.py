def solution(name):
    answer = 0
    
    num_list = [min(abs(ord('A')-ord(n)), 26-abs(ord('A')-ord(n))) for n in name]
    #상하로 갯수 미리 세서 걍 다 더해놓기.
    answer += sum(num_list)
    min_move = len(name) - 1
    
    for i, c in enumerate(name):
        
        next_i = i+1
        
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        # 각 문자부터 'A..'문자가 있을경우 몇번씩 조이스틱쓰는지 체크
        min_move = min(min_move, 2*i+ len(name)-next_i, 2*(len(name)-next_i)+i)
    return answer+min_move