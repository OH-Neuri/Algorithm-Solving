from collections import deque
def solution(begin, target, words):
    # 단어가 없는 경우
    if target not in words:
        return 0
    
    def BFS(word, target):
        
        q = deque()
        q.append((word,0))
        
        while q:
            b_word, c = q.popleft() # 현재 단어, 횟수
            
            if b_word == target:
                return c
            
            for w in words: 
                cnt = 0
                for b, x in zip(b_word, w):  # 문자 하나씩 비교
                    if b!=x:
                        cnt +=1
                if cnt == 1:
                    q.append((w,c+1))
                    
    answer = BFS(begin, target)
    return answer