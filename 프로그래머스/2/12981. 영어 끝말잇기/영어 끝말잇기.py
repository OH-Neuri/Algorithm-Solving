import math
def solution(n, words):
    answer = []
    word_list = []
    word_list.append(words[0])
    for i in range(1, len(words)):
        # 말했던 단어이거나 이어서 말하지 못한 경우
        if words[i] in word_list or word_list[-1][-1] != words[i][0]:

            return  [i % n + 1, i // n + 1]
        else:
            word_list.append(words[i])
    return [0,0]    