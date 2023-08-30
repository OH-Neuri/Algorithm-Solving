def solution(record):
    enter = " 님이 들어왔습니다."
    leave = " 님이 나갔습니다."
    nickname = {}
    sequence = []
    answer=[]
    for x in record:
        x = x.split(" ")
        if x[0] =="Enter":
            sequence.append(x[1]+enter)
            nickname[x[1]]=x[2]
        if x[0] == "Leave":
            sequence.append(x[1]+leave)
        if x[0] == "Change":
            nickname[x[1]]=x[2]

    for x in sequence:
        x = x.split(" ")
        answer.append(nickname[x[0]]+x[1]+" "+x[2])
    return answer