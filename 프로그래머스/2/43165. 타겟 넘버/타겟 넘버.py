def solution(numbers, target):
    global answer
    answer = 0
        
    def DFS(depth, t, summ):
        global answer
        
        if depth == len(numbers):
            if summ == t:
                answer +=1
            return 

        DFS(depth+1, t, summ + numbers[depth])
        DFS(depth+1, t, summ - numbers[depth])

    DFS(0,target,0)
    
    return answer