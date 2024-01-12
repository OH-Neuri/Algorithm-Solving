                
def solution(tickets):
    answer = ["ICN"]
    
    t = sorted(tickets, key=lambda x:(x[0],x[1]))
    visited = [ False for _ in range(len(t))]
    
    s = "ICN"
    e = ""
    l = len(t)
    
    def DFS(e, depth):
        if depth == len(t)-1:
            return True

        for i in range(l):
            if e == t[i][0] and not visited[i]:
                e = t[i][1]
                visited[i] = True
                answer.append(e)
                if DFS(e,depth+1):
                    return True
                e = t[i][0]
                visited[i] = False
                answer.pop()
                
    for i in range(l):
        if t[i][0] == s:
            e = t[i][1]
            visited[i] = True
            answer.append(e)
            DFS(e,0)
            if len(answer) == l+1:
                return answer
            visited[i] = False
            answer.pop()
    
    return answer