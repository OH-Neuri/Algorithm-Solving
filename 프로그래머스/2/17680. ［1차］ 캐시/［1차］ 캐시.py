from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    # 캐시 크기가 0일 때
    if cacheSize == 0:  
        return len(cities) * 5

    for c in cities:
        # 대소문자 구분하지 않기 위해 모두 소문자로 변경
        c = c.lower()  
        # 캐시에 있는 데이터라면
        if c in cache:  
            answer += 1
             # 데이터 삭제
            cache.remove(c) 
        # 캐시에 없는 데이터라면
        else:  
            answer += 5
        cache.append(c)
    return answer