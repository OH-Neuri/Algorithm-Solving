def solution(s):
    # 구간이 겹치면 압축한다 -> 문자열 길이에서 구간 값 뺴기
    # 각 단위별 문자열 길이는 dict 에 저장한다.
    l = len(s)
    if l == 1:
        return 1 
    str_length = {}
    for i in range(1,l//2+1):
        s_len = l
        cnt= 0
        flag = False
        for j in range(0,l,i):
            if s[j:j+i]==s[j+i:j+i+i]:
                s_len -= i
                if not flag:
                    flag = True
                if flag:
                    cnt+=1
                    print(s[j:j+i],s[j+i:j+i+i],cnt)
            else:
                flag = False
                if cnt>0:
                    s_len += len(str(cnt+1))
                cnt=0
        str_length[i] = s_len+cnt
    print(str_length)
    return min(str_length.values())