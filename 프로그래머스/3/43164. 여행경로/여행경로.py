def solution(tickets):
    answer = []
    l = len(tickets)
    visited = [False] *l
    tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    
    def flight_path(depth, path, idx):
        if depth == l:
            answer.append(path)
            return True
        
        for i in range(l):
            if not visited[i] and tickets[i][0] == path:
                visited[i] = True
                answer.append(path)
                if flight_path(depth+1, tickets[i][1], i):
                    return
                
        for i in visited:
            if not i:
                visited[idx] = False
                answer.pop()
                return
            
    for i in range(l):
        if tickets[i][0] == 'ICN':
            visited[i] = True
            answer.append('ICN')
            flight_path(1, tickets[i][1], i)
            if len(answer)-1!=l:
                visited = [False] *l
                answer = []
                continue
            break
            
    return answer

