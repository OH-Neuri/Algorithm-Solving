from collections import deque
def solution(begin, target, words):
    # begin하고 words 비교해서 하나만 다른지 확인해야함
    answer = 0
    words_dict = {}
    # 하나만 다른지 확인하기
    def isOne(b, w):
        check = 0
        for i in range(len(b)):
            if b[i]!=w[i]:
                check +=1
        if check == 1:
            return True
        else : return False

    # BFS
    def BFS(word, cnt):
        q = deque()
        q.append([word,cnt])
        
         # 기저 : begin == target, cnt 반환
        while q:
            curr, c = q.popleft()
            if curr == target:
                return c
            
            for i in range(len(words)):
                # 들어가기 : 첫방문, 알파벳 하나만 다를 때
                if words_dict.get(words[i],0) == 0 and isOne(curr,words[i]): 
                    words_dict[words[i]] = 1
                    q.append([words[i],c+1])
        return 0
    answer = BFS(begin,0)
    return answer