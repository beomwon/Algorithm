def solution(n, k):
    answer, t = [], k
    while True:
        answer.append(t)
        t += k
        if n < t:
            break
    return answer