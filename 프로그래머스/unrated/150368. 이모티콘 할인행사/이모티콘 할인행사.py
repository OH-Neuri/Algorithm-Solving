ans_cnt = 0
ans_purc = 0
def solution(users, emoticons):
    l = len(emoticons)
    search_emo([0] * len(users), users, emoticons, 0, l)
    answer = [ans_cnt, ans_purc]
    return answer


def search_emo(tot_purc, users, emoticons, d, l):
    global ans_cnt, ans_purc
    if d == l:
        cnt, purc = 0, 0
        for j, user in enumerate(users):
            if tot_purc[j] >= user[1]:
                cnt += 1
            else:
                purc += tot_purc[j]
        if cnt > ans_cnt:
            ans_cnt = cnt
            ans_purc = purc
        elif cnt == ans_cnt and purc > ans_purc:
            ans_purc = purc
        return

    value = emoticons[d]  # 이모티콘 정가

    for i in range(1, 5):
        update_purc = tot_purc[:]
        disc_val = value * (1 - 0.1 * i)  # 이모티콘 할인가
        for j, user in enumerate(users):
            if i * 10 >= user[0]:
                update_purc[j] += disc_val
        search_emo(update_purc, users, emoticons, d + 1, l)