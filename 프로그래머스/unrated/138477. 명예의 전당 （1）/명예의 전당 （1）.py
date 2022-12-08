def solution(k, score):
    temp, answer = [], []
    for v in score:
        temp.append(v)
        temp = sorted(temp, reverse=True)
        if len(temp) < k:
            answer.append(temp[-1])
        else:
            answer.append(temp[k-1])
        
    return answer