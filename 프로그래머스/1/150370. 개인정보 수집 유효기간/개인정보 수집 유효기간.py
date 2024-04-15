def solution(today, terms, privacies):
    answer = []
    t_y,t_m,t_d = [date for date in today.split('.')]
    today = int(f'{t_y}{t_m}{t_d}')
    
    dic = {}
    for term in terms :
        term_a,term_d = term.split()
        dic[term_a]=int(term_d)
        
    for i,privacy in enumerate(privacies) :
        fulldate, term_a = privacy.split()
        y,m,d = [date for date in fulldate.split('.')]
        m = int(m) + dic[term_a]
        dy,dm = divmod(m,12)
        if not dm :
            dy -= 1
            dm += 12
        y = int(y) + dy
        if dm < 10 :
            m = '0' + str(dm)
        else :
            m = str(dm)

        d_day = int(f'{y}{m}{d}')

        if d_day <= today :
            answer.append(i+1)
    return answer