from collections import deque
def solution(progresses, speeds):
    # 각 프로세스에 대해 작업진도가 100이상이 되는 시간을 구한다.
    # q = deque(progresses)
    # # 배포 가능한 작업의 개수 구하기
    # while q:
    #     progress = q.popleft()
    #     cnt = 0
    
    #     while progress <100:
    
    answer = []
    t = deque()
    for i in range(len(progresses)):
        cnt = 0
        while progresses[i] < 100:
            cnt+=1
            progresses[i] = progresses[i] + speeds[i]
        t.append(cnt)   
        
    while t:
        cnt = 1
        curr = t.popleft()
        while t and curr >= t[0]:
            cnt+=1
            t.popleft()
        answer.append(cnt)
        
    return answer