def solution(n):
	# 어태까지의 queen 위치 ls, 내가 두려는 위치 new
    def check(ls, new):
        for i in range(len(ls)):
        	# 같은 열에 퀸을 둔 적이 있거나, 대각 위치에 둔 적이 있다면, return False
            if new == ls[i] or (len(ls)-i) == abs(ls[i]-new):
                return False
        return True
    def dfs(n, ls):
        if len(ls) == n:
            return 1
        
        cnt = 0
        for i in range(n):
            if check(ls, i):
                cnt += dfs(n, ls+[i])
        return cnt
        
    return dfs(n, [])