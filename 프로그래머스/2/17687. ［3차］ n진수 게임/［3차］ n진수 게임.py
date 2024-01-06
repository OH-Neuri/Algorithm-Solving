def solution(n, t, m, p):
    answer = ''
    
    def convert(num, base):
        T = "0123456789ABCDEF"
        q , r = divmod(num,base)
        if q == 0:
            return T[r]
        else:
            return convert(q, base) + T[r]

    num = ''
    i = 0
    while len(num) < t*m:
        num += convert(i,n)
        i+=1
        
    for i in range(0,len(num),m):
        answer += num[i+p-1]
        if len(answer) == t:
            return answer
    
    return answer


