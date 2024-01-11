def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        flag = False
        idx = 0
        for j in range(len(s)):
            # 안되는 경우
            if skill[idx] != s[j] and s[j] in skill:
                flag = True
                break
            # 맞는 경우
            if idx == len(skill)-1:
                break
            if skill[idx] == s[j]:
                idx +=1
        if not flag:
            answer +=1        
    return answer