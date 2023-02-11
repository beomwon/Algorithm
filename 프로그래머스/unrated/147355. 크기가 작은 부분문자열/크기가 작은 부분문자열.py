def solution(t, p):
    answer = 0
    p_len = len(p)
    for i in range(len(t)-p_len+1):
        if t[i:i+p_len] <= p:
            answer += 1
    return answer