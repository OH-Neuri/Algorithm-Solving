def solution(s):
    answer = -1
    # 방법
    st = []
    l = len(s)
    for i in s:
        #넣는다
        st.append(i)
        #뺀다
        while len(st) >= 2 and st[-2]==st[-1]:
            st.pop()
            st.pop()
    
    return 1 if len(st)==0 else 0