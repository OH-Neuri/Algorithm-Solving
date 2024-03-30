def solution(s):
    num_dict = {"zero":0,"one":1, "two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    answer = []
    num_str = ""
    for word in s:
        if word.isdigit():
            answer.append(int(word))
        else:
            num_str += word
            if num_str in num_dict:
                answer.append(num_dict[num_str])
                num_str = ""

    return int(''.join(map(str, answer)))