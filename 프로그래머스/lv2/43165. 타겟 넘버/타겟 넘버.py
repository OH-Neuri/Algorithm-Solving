def solution(numbers, target):
    answer = 0
    
    def DFS(dept, val):
        nonlocal answer
        
        if dept == len(numbers):
            if val == target:
                answer +=1
            return
        
        DFS(dept+1, val+numbers[dept])
        DFS(dept+1, val-numbers[dept])
        
    DFS(0,0)
    return answer