def solution(files):
    # 방법 1.헤더, 넘버, 테일 구분한다음
    # 딕셔너리에 value로 정렬한다음 키를 반환하자
    # 방법 2. 바로 정렬 갈기고 반환하자
    file_dic={}
    while files:
        a = files.pop(0)
        head = ""
        temp = ""
        for i in a:
            if i.isdigit():
                temp +=i
            # temp 나올 때까지
            elif not temp: 
                head+=i
                pass
            else:
                break
        file_dic[a] = (head.upper(),int(temp))
    return sorted(file_dic.keys(), key = lambda x: (file_dic[x]))