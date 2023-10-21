import numpy as np
 
def solution(places):
    answer = []
    for place in places:
        exam_list = []
        for p in place:
            exam_list.append(list(p))
        exam_arr = np.array(exam_list)
        r_index, c_index = np.where(exam_arr == 'P')
        if len(r_index) == 0:
            answer.append(1)
            continue
        
        b_break = True
        for i in range(len(r_index)-1):
            for j in range(i+1, len(r_index)):
                if (abs(r_index[i] - r_index[j])) + (abs(c_index[i] - c_index[j])) < 3:
                    if c_index[i] < c_index[j] :
                        cut = exam_arr[r_index[i]:r_index[j]+1, c_index[i]:c_index[j]+1]
                        if 'X' not in cut or 'O' in cut:
                            answer.append(0)
                            b_break = False
                            break
                    else:
                        cut = exam_arr[r_index[i]:r_index[j]+1, c_index[j]:c_index[i]+1]
                        if 'X' not in cut or 'O' in cut:
                            answer.append(0)
                            b_break = False
                            break
                            
            if b_break == False:
                break
        if b_break == True:        
            answer.append(1)
    return answer