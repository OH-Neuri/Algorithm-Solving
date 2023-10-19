def replacement(data) :
    data = data.replace('C#', 'c')
    data = data.replace('D#', 'd')
    data = data.replace('F#', 'f')
    data = data.replace('G#', 'g')
    data = data.replace('A#', 'a')

    return data

def solution(m, musicinfos) :
    answer = ''
    m = replacement(m)

    max_time = 0
    for music in musicinfos :
        start, end, name, info = music.split(",")
        info = replacement(info)

        play_time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
        index = 0
        value = ''
        time = play_time
        while time :
            value += info[index]
            if index + 1 == len(info) :
                index = -1
            index += 1
            time -= 1

        if m in value :
            if answer :
                if max_time >= play_time :
                    continue
            max_time = play_time
            answer = name

    if answer :
        return answer
    else :
        return '(None)'